# Rename the file to main.py 

# ------------------------------------------------------
# 1) IMPORTS & SETUP
# ------------------------------------------------------
import colorama
from colorama import Fore, Style
from textblob import TextBlob
# - Import colorama for colored text
# - Import specific color constants (e.g., Fore, Style)
# - Import textblob for sentiment analysis
# - Initialize colorama for cross-platform color support

# ------------------------------------------------------
# 2) INITIAL GREETING
colorama.init()
# ------------------------------------------------------
# - Print a welcome message using a color (e.g., Fore.CYAN)
# - Include emojis (e.g., '👋', '🕵️') for a fun greeting
print(f"{Fore.CYAN}👋🕵️ Welcome to Sentiment Spy!🕵️{Style.RESET_ALL}")
# ------------------------------------------------------
# 3) USER NAME INPUT
un=input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL} ").strip()
if not un:
    un="Mystery Agent"
# ------------------------------------------------------
# - Prompt the user for their name
# - Strip extra whitespace
# - If empty, default to "Mystery Agent"

# ------------------------------------------------------
# 4) CONVERSATION HISTORY
ch=[]
print(f"\n{Fore.CYAN}Hello Agent{un}!")
print(f"Type in your sentence and I will analyze it with TextBlob and show you the sentiment.")
print(f"Type{Fore.YELLOW}'reset'{Fore.CYAN},{Fore.YELLOW}'history'{Fore.CYAN},{Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}")
# ------------------------------------------------------
# - Create a structure (e.g., list) to store each user input
#   along with its polarity and sentiment type
# - For example: (user_text, polarity, sentiment_type)

# ------------------------------------------------------
# 5) INSTRUCTIONS
# ------------------------------------------------------
# - Print instructions to the user describing the available
#   commands (e.g., 'reset', 'history', 'exit')

# ------------------------------------------------------
# 6) MAIN INTERACTION LOOP
while True:
    un=input(f"{Fore.GREEN}>>{Style.RESET_ALL}").strip()
    if not un:
        print(f"{Fore.RED}PLease enter some text or a valid command.{Style.RESET_ALL}")
        continue
    if un.lower()=="exit":
        print(f"\n{Fore.BLUE}Exiting Sentiment Spy. Farewell, Agent{un}!{Style.RESET_ALL}")
        break
    elif un.lower()=="reset":
        ch.clear()
        print(f"{Fore.CYAN}ALL conversation history cleared!{Style.RESET_ALL}")
        continue
    elif un.lower()=="history":
        if not ch:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")
            for idx,(text,polarity,sentiment_type) in enumerate(ch,start=1):
                if sentiment_type=="Positive":
                    color=Fore.GREEN
                    emoji="😊" 
                elif sentiment_type=="Negative":
                    color=Fore.RED
                    emoji="😢" 
                else:
                    sentiment_type=="Neutral"
                    color=Fore.YELLOW
                    emoji="😐"
                print(f"{idx}.{color}{emoji} {text}"f"(Polarity:{polarity:2f},{sentiment_type}){Style.RESET_ALL}") 
                continue
    polarity=TextBlob(un).sentiment.polarity
    if polarity>0.25:
        sentiment_type="Positive" 
        color=Fore.GREEN
        emoji="😊"
    elif polarity<-0.25:
        sentiment_type="Negative" 
        color=Fore.RED
        emoji="😢" 
    else:
        sentiment_type="Neutral" 
        color=Fore.YELLOW
        emoji="😐" 
    ch.append((un,polarity,sentiment_type)) 
    print(f"{color}{emoji}{sentiment_type} sentiment detected!"f"(Polarity:{polarity:.2f}){Style.RESET_ALL}")       


# ------------------------------------------------------
# - Use a 'while True:' loop to repeatedly prompt the user
# - Read input and strip whitespace
# - If empty, notify the user and continue

#     6.1) 'exit' COMMAND
#         - If user_input.lower() == 'exit':
#           - Print a farewell message
#           - Break out of the loop to end the program

#     6.2) 'reset' COMMAND
#         - Clear the conversation history
#         - Print a message confirming reset

#     6.3) 'history' COMMAND
#         - If no history, print a message indicating so
#         - Otherwise, print each conversation entry
#           - Show text, polarity (formatted), and sentiment type
#           - Use color and emojis based on sentiment
#         - Continue the loop

#     6.4) SENTIMENT ANALYSIS
#         - If the input is not a command, analyze sentiment
#         - Use TextBlob(user_input).sentiment.polarity to get a float
#           between -1.0 and +1.0
#         - Define thresholds:
#             > 0.25 -> Positive
#             < -0.25 -> Negative
#             Otherwise -> Neutral
#         - Assign color and emoji accordingly (e.g., GREEN/😊, RED/😢, YELLOW/😐)
#         - Append the tuple (text, polarity, sentiment_type) to the history
#         - Print a result message showing sentiment type and polarity

# ------------------------------------------------------
# END
# ------------------------------------------------------
# - The program terminates when 'exit' is typed
# - No additional code is shown beyond these comments
