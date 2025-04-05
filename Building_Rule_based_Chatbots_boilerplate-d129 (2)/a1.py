#name the file as main.py , uncomment the imports and basic functions, complete  the code by writing remainig functions 

import re, random
from colorama import Fore, init

# # Initialize colorama (autoreset ensures each print resets after use)
init(autoreset=True)

# # Destination & joke data
destinations ={
     "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
     "cities": ["Tokyo", "Paris", "New York"]
} 
jokes = [
     "Why don't programmers like nature? Too many bugs!",
"Why did the computer go to the doctor? Because it had a virus!",
"Why do travelers always feel warm? Because of all their hot spots!"
]

# # Helper function to normalize user input (remove extra spaces, make lowercase)
def normalize_input(text):
 return re.sub(r"\s+", " ", text.strip().lower())

# Provide travel recommendations (recursive if user rejects suggestions)
def recommend():
 print(Fore.CYAN+"TravelBot: Beaches, mountains or cities?")
 pref=input(Fore.YELLOW+"You:")
 pref=normalize_input(pref)
 if pref in destinations:
  suggestion=random.choice(destinations[pref])
  print(Fore.GREEN+f"TravelBot: How about{suggestion}?")
  print(Fore.CYAN+"TravelBot: Do you like it? (yes/no)")
  answer=input(Fore.YELLOW+"You:").lower()
  if answer=="yes":
   print(Fore.GREEN+f"TravelBot: Awsome! Enjoy {suggestion}!")
  elif answer=="no":
   print(Fore.RED+f"TravelBot: Let's try another one.")
  else:
   print(Fore.RED+f"TravelBot: I'll suggest again.")
 else:
  print(Fore.RED+"TravelBot: Sorry, I don't have that type of destination") 
  show_help()
# Offer packing tips based on user’s destination and duration
def packing_tips():
 print(Fore.CYAN+"TravelBot: Where to?")
 location=normalize_input(input(Fore.YELLOW+"You:"))
 print(Fore.CYAN+"TravelBot: How many days?")
 days=input(Fore.YELLOW+"You:")
 print(Fore.GREEN+f"TravelBot: Packing tips for {days} in {location}:")
 print(Fore.GREEN+"-Pack versatile clothes")
 print(Fore.GREEN+"-Bring chargers/adapters")
 print(Fore.GREEN+"-Check the weather forecast")
# Tell a random joke
def tell_joke():
 print(Fore.YELLOW+f"TravelBot:{random.choice(jokes)}")
# Display help menu
def show_help():
 print(Fore.MAGENTA+"\nI can")
 print(Fore.GREEN+"-Suggest travel spots (say 'recommendation')")
 print(Fore.GREEN+"-Offer packing tips (say 'packing')")
 print(Fore.GREEN+"-Tell a joke (say 'joke')")
 print(Fore.CYAN+"Type 'exit' or 'bye' to end.\n")
# Main chat loop
def chat():
 print(Fore.CYAN+"Hello! I am TravelBot.")
 name=input(Fore.YELLOW+"Your name?")
 print(Fore.GREEN+f"Nice to meet you, {name}!")
 show_help()
 while True:
  ui=input(Fore.YELLOW+f"{name}: ")
  ui=normalize_input(ui)
  if "recommend" in ui or "suggest" in ui:
   recommend()
  elif "pack" in ui or "packing" in ui:
   packing_tips()
  elif "joke" in ui or "jokes" in ui:
   tell_joke()
  elif "help" in ui:
   show_help()
  elif "exit" in ui or "bye" in ui:
   print(Fore.CYAN+"TravelBot: Safe travel! Goodbye!") 
   break 
  else:
   print(Fore.RED+"TravelBot: Could you rephrase?")

# Run the chatbot
if __name__ == "__main__":
 chat()
