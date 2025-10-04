import os
from google import genai
from google.genai import types
import config
from colorama import init, Fore, Style
#Initialize coloram
init(autoreset=True)
#initialize Gemini API client
GEMINI_API_KEY = "AIzaSyBTecMs4bgUrkSD8yMPwJ76TtPQapC7Bmg"
client = genai.Client(api_key=GEMINI_API_KEY)
def generate_response(prompt, temperature=0.3):
    """Generate a response from Gemini API."""
    try:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        config_params = types.GenerateContentConfig(temperature=temperature)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=contents, config=config_params)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
#Step 1: Get essay details
def get_essay_details():
    print(Fore.CYAN+"\n=== AI Writing Assistant ===\n")   
    #Gather user information for essay
    topic= input(Fore.YELLOW+"What is the topic of your essay?")
    essay_type=input(Fore.YELLOW+"What type of essay are you writing? (e.g Agumentative, Expository, Descriptive, Persuasive, Analytical)")
    #Modified section for selecting word count
    print(Fore.GREEN+"\nSelect the desired essay word count:")
    print(Fore.GREEN+"1.300 words")
    print(Fore.GREEN+"2.900 words")
    print(Fore.GREEN+"3.1200 words")
    print(Fore.GREEN+"4.2000 words")
    word_count_choice=input(Fore.YELLOW+"Please enter the number corresponding to your choice:")
    word_count_dict={"1":"300","2":"900","3":"1200","4":"2000"}
    length=word_count_dict.get(word_count_choice,"300")#Default to 300 words if invalid input
    target_audience=input(Fore.YELLOW+"Who is the target audience for the essay? (e.g., High school students, Collage professors)")
    specific_points=(Fore. YELLOW+"Do you have any specific points that must be included in the essay?")
    #Additional details
    stance=input(Fore.YELLOW+"What is your stance on the topic? (e.g., For, Against, Neutral)")
    reference=input(Fore.YELLOW+"Do you have any references for the essay?")
    writing_style=input(Fore.YELLOW+"Do you have an preferences for writing style? (e.g., Formal, Conversation, Academic, Creative)")
    #Ask for outline preference
    outline_needed=input(Fore.YELLOW+"Would you like the AI to suggest an outline first? (Yes/No)").lower()
    #Return the gathered information
    return{
        "topic":topic,
        "essay_type":essay_type,
        "target_audience":target_audience,
        "specific_point":specific_points,
        "stance":stance,
        "references":reference,
        "writing_style":writing_style,
        "outline_needed":outline_needed
    }
#Step 2:Generate Essay Context
def generate_essay_content(details):
    # Ask for creative vs structured temperature preference
    temperature = float(input(Fore.YELLOW + "Do you prefer a more creative and open-ended response (higher temp, e.g., 0.7) or a structured response (lower temp, e.g., 0.2)? Enter temperature value: "))
    #Start with generating intro
    intro_prompt=f"write an introduction for an {details['essay_type']} essay about {details['topic']} on the topic of {details['stance']}."
    intro=generate_response(intro_prompt,temperature)
    print(Fore.CYAN + "\n=== Generate Introduction ===")
    print(Fore.GREEN + intro)
    #Ask if user wants full body or step-by-step body
    body_style=input(Fore.YELLOW + "Would you like the AI to write the body step-by-step or generate a full draft? (Step-by-step/Full draft):").lower()
    #Generate body content based on style
    if body_style=="full draft":
        body_prompt=f"Write a detailed {details['essay_type']} essay about {details['topic']} with the stance of {details['stance']}."
        body=generate_response(body_prompt,temperature)
        print(Fore.CYAN+"\n=== Generate Full Body ===")
        print(Fore.GREEN + body)
    else:
        body_step_prompt=f"Write a step-by-step argument for the essay on {details['topic']} with the stance of {details['stance']}. Provide evidence and reasoning for each step"
        body_step=generate_response(body_step_prompt,temperature)
        print(Fore.CYAN+"\n=== Generate Step-by-step body ===")
        print(Fore.GREEN + body_step)
    #conclusion generation
    conclusion_prompt=f"Write a conclusion for an {details['essay_type']} essay about {details['topic']} with the stance of {details['stance']}."
    conclusion=generate_response(conclusion_prompt,temperature)
    print(Fore.CYAN+"\n=== Generate Conclusion ===")
    print(Fore.GREEN + conclusion) 
#Step 3: Feedback and Refinement
def feedback_and_refinement():
   # Get user feedback on the content
   satisfaction = input(Fore.YELLOW + "How satisfied are you with the generated content? (Rate from 1 to 5 stars): ")
   if satisfaction != "5":
      print(Fore.YELLOW + "Please provide feedback on how we can improve the content (tone, structure, etc.): ")
      feedback = input(Fore.YELLOW)
      print(Fore.CYAN + f"\nThank you for your feedback! We will refine the essay based on your input: {feedback}")
   else:
      print(Fore.CYAN + "\nThank you! The essay looks good.")
# Main Function
def run_activity():
   print(Fore.CYAN + "\nWelcome to the AI Writing Assistant!")
   # Get essay details from user
   details = get_essay_details()
   # Generate the essay content based on the details
   generate_essay_content(details)
   # Ask for feedback and refine
   feedback_and_refinement()
# Run the Activity
if __name__ == "__main__":
  run_activity()     