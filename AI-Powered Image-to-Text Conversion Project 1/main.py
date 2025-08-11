import requests
from PIL import Image
import io
import os
from colorama import init, Fore, Style
import json
#initialize colorama for colorful output
#Utility function to send API requests
API_KEY = "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"
def query_hf_api(api_url, payload=None, files=None, method="post"):
  headers = {"Authorization": f"Bearer {API_KEY}"}
  try:
     if method.lower()=="post":
        #When files provided, send them along with the payload
        response=requests.post(api_url, headers=headers, json=payload, files=files)
     else:
        response=requests.get(api_url, headers=headers, params=payload)
     if response.status_code != 200:
        raise Exception(f"Status {response.status_code}: {response.text}")
     return response.content       
  except Exception as e:
     print(f"{Fore.RED} Error while calling API: {e}")
     raise
#Task: Get a basic caption from an image using an image captioning model
def get_basic_caption(image, model="nlpconnect/vit-gpt2-image-captioning"):
   print(f"{Fore.YELLOW}????? Generating basic caption using vit-gpt2-image-captioning...")  
   api_url=f""
   buffered=io.BytesIO()
   #Save as JPEG(this model works well with Jpeg images)
   image.save(buffered, format="JPEG")
   buffered.seek(0)
   headers={"Authorization": f"Bearer {API_KEY}"}
   response=requests.post(api_url, headers=headers, data=buffered.read())
   result=response.json()
   if isinstance(result, dict) and "error" in result:
      return f"[Error] {result['error']}"
   #Expecting result to be a list of dicts with 'generated_text'
   caption=result[0].get("generated_text", "No caption generated.")
   return caption
