import requests
api_key="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"
def classify_text(text):
    API_URL="https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    headers={"Authorization":f"Bearer {api_key}"}
    payload={"inputs":text}
    response=requests.post(API_URL,headers=headers,json=payload)
    return response.json()
if __name__=="__main__":
    sample_text="I love using Hugging APIs!"
    result=classify_text(sample_text)
    print(result)