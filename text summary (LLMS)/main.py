import requests
from colorama import Fore,Style,init
#initialize colorama for colored terminal output
init(autoreset=True)
#default model name that can be easily changed
DM="google/pegasus-xsum"
def BUILD_API_URL(model_name):
    return f"https://api-inference.huggingface.co/models/{model_name}"
HF_API_KEY="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"
def query(payload, model_name=DM):
    #Send POST request to the HUgging FAce API using the specified model
    api_url=BUILD_API_URL(model_name)
    headers={"Authorization":f"Bearer {HF_API_KEY}"}
    response=requests.post(api_url,headers=headers,json=payload)
    return response.json()
def summary(text,min_length,max_length,model_name=DM):
    payload={"inputs":text,"parameters":{"min_length":min_length,"max_length":max_length}}
    print(Fore.BLUE+Style.BRIGHT+f"\n?????? Performing AI summarization using model:{model_name}")
    result=query(payload,model_name=model_name)
    #Check if the response has the expected format
    if isinstance(result, list) and result and "summary_text" in result[0]:
        return result[0]["summary_text"]
    else:
        print(Fore.RED+"Error in summarization response:",result)
        return None
if __name__=="__main__":  
    print(Fore.YELLOW + Style.BRIGHT + "👋🏼 Hi there! What's your name?")
    user_name = input("Your name: ").strip()
    if user_name == "":
      user_name = "User"
    print(Fore.GREEN + f"\nWelcome, {user_name}! Let's give your text some AI magic 🪄")
    # Prompt the user for text input
    print(Fore.YELLOW + Style.BRIGHT + "\nPlease enter the text you want to summarize:")
    user_text = input("> ").strip()
    if not user_text:
      print(Fore.RED + "❌ No text provided. Exiting.")
      exit()
    # Ask the user for the model they want to use
    print(Fore.YELLOW + "\n🧠 Enter the model name you want to use (e.g., facebook/bart-large-cnn):")
    print("(Press Enter to use the default model)")
    model_choice = input("Model name: ").strip()
    if model_choice == "":
      model_choice = DM
    # Ask for summarization style
    print(Fore.YELLOW + "\n✨ Choose your summarization style:")
    print("1. Concise Summary (quick & concise)")
    print("2. Enhanced Summary (more detailed and refined)")
    style_choice = input("Enter 1 or 2: ").strip()
    if style_choice == "2":
       print(Fore.BLUE + "🔍 Enhancing summarization process... 🧵🧠")
       min_length = 80
       max_length = 200
    else:
       print(Fore.BLUE + "✏️ Using standard summarization settings... ✏️")
       min_length = 50
       max_length = 100
    # Generate the summary using the chosen model and settings
    summary = summary(user_text, min_length, max_length, model_name=model_choice)
    if summary:
      print(Fore.GREEN + Style.BRIGHT + f"\n📝 AI Summary Output for {user_name}:\n")
      print(Fore.GREEN + summary)
    else:
      print(Fore.RED + "❌ Failed to generate summary.")
    

    

