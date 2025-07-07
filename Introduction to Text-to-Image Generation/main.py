import requests
from PIL import Image
from io import BytesIO
#Dfine the api enpoint as a constant
API_URL="https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
API_KEY="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"
def generate_image_from_text(prompt:str)->Image.Image:
    headers={"Authorization":f"Bearer{API_KEY}"}
    payload={"input":prompt}
    try:
        response=requests.post(API_URL,headers=headers,json=payload,timeout=30)
        response.raise_for_status#Raise an error for bad status codes
        #Check if the response content is an image
        if 'image' in response.headers.get('Content-Type',''):
            image=image.open(BytesIO(response.content))
            return image
        else:
            raise Exception("The response is not an image It might be an error message")
    except requests.exception.RequestException as e:
        raise Exception(f"Request failed:{e}")    
def main():
    print("Welcome to the Text-to-image Generator!")
    print("Type 'exit' to quit the program.\n")
    while True:
        prompt=input("Enter a description for the image you want to generate:\n").strip()
        if prompt.lower()=="exit":
            print("Goodbye")
            break
        print("\nGenerating image...\n")
        try:
            image=generate_image_from_text(prompt)
            image.show()
            save_option=input("Do you want to save this image?(yes/no):").strip().lower()
            if save_option=="yes":
                file_name=input("Enter name for the image file(without extension):").strip() or "generated_image"
                #Basic validation for name
                file_name="".join(c for c in file_name if c.isalnum() or c in ('_','-')).rstrip()
                image.save(f"{file_name}.png")
                print("image saved")
        except Exception as e:
            print("An error occurred:{e}\n") 
if __name__=="__main__":
    main()                   
