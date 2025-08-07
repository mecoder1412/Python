import requests
from io import BytesIO
# Define the API endpoint and key
model_ID="nlpconnect/vit-gpt2-image-captioning"
API_URL = "https://api-inference.huggingface.co/models/{model_ID}"
API_KEY = "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"
headers = {"Authorization": f"Bearer {API_KEY}"}
image_source="test.png"#Hardcoded filename
#Load image bytes
try:
    with open(image_source,"rb") as f:
        image_bytes=f.read()
except Exception as e:
    print(f"Could not load image from {image_source}.\nError:{e}")
#Send request to the Hugging Face Interface API
response=requests.post(API_URL, headers=headers, data=image_bytes)
result=response.json()
#Check for errors
if isinstance(result,dict) and "error" in result:
    print(f"[Error] {result['error']}")
#Extract caption
caption=result[0].get("generated_text","No caption found")
print("Image:",image_source)
print("Caption:",caption)


        