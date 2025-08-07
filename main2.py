import requests, base64
from PIL import Image
from io import BytesIO

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-inpainting"
API_KEY = "hf_xxx"  # Replace with your key

def generate_image_from_text(prompt, image_path, mask_path):
    headers = {"Authorization": f"Bearer {API_KEY}"}

    # Read and encode images as base64
    with open(image_path, "rb") as f:
        base_image = base64.b64encode(f.read()).decode("utf-8")
    with open(mask_path, "rb") as f:
        mask_image = base64.b64encode(f.read()).decode("utf-8")

    payload = {
        "inputs": prompt,
        "parameters": {
            "image": base_image,
            "mask": mask_image
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        # Hugging Face returns a list with base64 image bytes
        image_bytes = base64.b64decode(result[0]["image_base64"])
        return Image.open(BytesIO(image_bytes))
    else:
        raise Exception(f"Request failed: {response.status_code} {response.text}")          

