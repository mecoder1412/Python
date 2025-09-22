# 1. IMPORT necessary libraries:
#    - google.genai (for interacting with the Gemini API)
#    - config (for managing API key)
import os
from google import genai
from google.genai import types
import config
# 2. DEFINE function generate_response(prompt, temperature=0.3):
#    - Initialize genai client using the API key from config
#    - Create content structure based on the prompt
#    - Send the prompt to Gemini API and return the generated response
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
# 3. DEFINE function bias_mitigation_activity():
#    - Print introductory message for bias mitigation activity
#    - Prompt user to input a prompt (e.g., "Describe the ideal doctor")
#    - Generate AI response to the initial prompt
#    - Prompt user to modify the prompt to make it more neutral
#    - Generate AI response to the modified (neutral) prompt
#    - Display both AI responses
def bias_mitigation_actity():
    print('\n=== BIAS MITIGATION ACTIVITY ===')
    prompt=input("Enter a prompt to explore bias (e.g., 'Describe the ideal doctor')")
    initial_response=generate_response(prompt) 
    print(f"\nInitial AI Response: {initial_response}")
    modified_prompt=input("Modify the prompt to make it more neutral (e.g., 'Describe the qualities of a doctor')")
    modified_response=generate_response(modified_prompt) 
    print(f"\n Modified AI Response (Neutral): {modified_response}")
# 4. DEFINE function token_limit_activity():
#    - Print introductory message for token limit activity
#    - Prompt user to input a long prompt (more than 300 words)
#    - Generate AI response to the long prompt
#    - Display a truncated portion of the response (limit output for demonstration)
#    - Prompt user to condense the long prompt into a shorter one
#    - Generate AI response to the shortened prompt
#    - Display the AI response to the shortened prompt
def token_limit_actity():
    print('\n=== TOKEN LIMIT ACTIVITY ===')
    long_prompt=input("Enter a long prompt (more than 300 words e.g., a detailed story)")
    long_response=generate_response(long_prompt) 
    print(f"\nLong prompt AI Response: {long_response[:500]}...")# Limit output for demonstration
    short_prompt=input("Now, condense the prompt and make it more concise:")
    short_response=generate_response(short_prompt) 
    print(f"\nAI Response to condensed prompt: {short_response}")
# 5. DEFINE function run_activity():
#    - Print introductory message for AI learning activity
#    - Prompt the user to choose between the bias mitigation activity or token limit activity
#    - If the user chooses "1", run bias_mitigation_activity()
#    - If the user chooses "2", run token_limit_activity()
#    - If the user enters an invalid choice, prompt them again

# 6. IF __name__ == "__main__":
#    - Call run_activity() to initiate the activity
def run_activity():
        #Runs the entire activity
        print("\n=== AI Learning Activity ===")
        #Choose sctivity
        activity_choice=input("which activity would you like to run? (1:Bias Mitigation, 2: Token Limits):")
        if activity_choice=="1":
            bias_mitigation_actity()
        elif activity_choice=="2":
            token_limit_actity()
        else:
            print("Invalid choice. Please choose either 1 or 2")
if __name__=="__main__":
    run_activity()