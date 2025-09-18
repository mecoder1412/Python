import os
import time
from google import genai
from google.genai import types
GEMINI_API_KEY = "AIzaSyBTecMs4bgUrkSD8yMPwJ76TtPQapC7Bmg"
def generate_response(prompt, temperature=0.5):
    #generate response from gemini API with specified temperature
    try:
        #initialize the client with API key FROM config module
        client = genai.Client(api_key=GEMINI_API_KEY)
        #Create the content structure
        contents=[
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=prompt)
                ],
            ),
        ]
        # Config generation parameter
        generate_content_config = types.GenerateContentConfig(
           temperature=temperature,
           response_mime_type="text/plain",
        )
        #generate content
        response = client.models.generate_content(
            model="gemini-2.0-flash", # Or replace with OpenAI GPT model if using GPT
            contents=contents,
            config=generate_content_config,
        )
        #Extract and return the response text
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"
def temperature_prompt_activity():
   """Interactive activity to explore temperature settings and instruction-based prompts."""
   print("=" * 80)
   print("ADVANCED PROMPT ENGINEERING: TEMPERATURE & INSTRUCTION-BASED PROMPTS")
   print("=" * 80)
   print("\nIn this activity, we'll explore:")
   print("1. How temperature affects AI creativity and randomness")
   print("2. How instruction-based prompts can control AI outputs")
   # Part 1: Temperature Exploration
   print("\n" + "-" * 40)
   print("PART 1: TEMPERATURE EXPLORATION")
   print("-" * 40)
   base_prompt = input("\nEnter a creative prompt (e.g., 'Write a short story about a robot learning to paint'): ")
   print("\nGenerating responses with different temperature settings...")
   print("\n--- LOW TEMPERATURE (0.1) - More Deterministic ---")
   low_temp_response=generate_response(base_prompt, temperature=0.1)
   print(low_temp_response)
   #Add a small delay between API calls to avoid rate limiting
   time.sleep(1)
   print("\n--- MEDIUM TEMPERATURE (0.5) - Balanced ---")
   medium_temp_response=generate_response(base_prompt, temperature=0.5)
   print(medium_temp_response)
   #Add a small delay between API calls to avoid rate limiting
   time.sleep(1)
   print("\n--- HIGH TEMPERATURE (0.9) - More Random/Creative ---")
   high_temp_response=generate_response(base_prompt, temperature=0.9)
   print(high_temp_response)
   #Add a small delay between API calls to avoid rate limiting
   time.sleep(1)
   #Part 2: Instruction- Based Prompts
   print("\n" + "-" * 40)
   print("PART 2: INSTRUCTION-BASED PROMPTS")
   print("-" * 40)
   print("\nNow, let's explore how specific instructions change the AI's output.")
   topic = input("\nChoose a topic (e.g., 'climate change', 'space exploration'): ")
   #Different instructions based prompt
   instructions = [
   f"Summarize the key facts about {topic} in 3-4 sentences.",
   f"Explain {topic} as if I'm a 10-year-old child.",
   f"Write a pro/con list about {topic}.",
   f"Create a fictional news headline from the year 2050 about {topic}."
   ]
   #display different instruction-basedoutput
   for i, instruction in enumerate(instructions,1):
       print(f"\n----- INSTRUCTION {i}: {instruction}----")
       response=generate_response(instruction, temperature=0.7)
       print(response)
       time.sleep(1)
   # Part 3: Combining Instructions and Temperature
   print("\n" + "-" * 40)
   print("PART 3: CREATING YOUR OWN INSTRUCTION-BASED PROMPTS")
   print("-" * 40)
   print("\nNow it's your turn! Create an instruction-based prompt and test it with different temperatures.")
   custom_instruction = input("\nEnter your instruction-based prompt: ")
   try:
       custom_temp=float(input("\n Set a temperature (0.1 to 1.0)"))
       if custom_temp<0.1 or custom_temp>1.0:
           print("invalid temperature. Using default 0.7")
           custom_temp=0.7
   except ValueError:
       print("Invalid input. Using default 0.7") 
       custom_temp=0.7
   print(f"\n--- YOUR CUSTOM PROMPT WITH TEMPERATURE {custom_temp} ---")
   custom_response = generate_response(custom_instruction, temperature=custom_temp)
   print(custom_response)
   
if __name__ == "__main__":
    temperature_prompt_activity()   