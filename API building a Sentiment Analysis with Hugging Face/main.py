import requests
#Hugging Face API URL for sentiment analysis
url="https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"
#replace with your Hugging Face API token
headers={"Authorization":"Bearer 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"}
#Sample text for sentiment analysis
text="I love this movie! It was fantstic."
#Send POST request to the Hugging Face API
response=requests.post(url,headers=headers,json={"inputs":text})
if response.status_code==200:
    #Parse the response JSON
    result=response.json()
    print(result)
    print(f"Sentiment:{result[0]} with confidence score: {result[0]}")
else:
    print(f"Error:{response.status_code}")