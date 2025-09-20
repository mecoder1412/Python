import os
from google import genai
from google.genai import types
import config
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
def reinforcement_learning_activity():
    #Conducts  the reinforcement learning activity.
    print("\n=== REINFORCEMENT LEARNING ACTIVITY ===\n")
    #Get user input for rating and feedback
    prompt=input("Entera prompt for the AI model (e.g, 'Describe the lion')")
    initial_response=generate_response(prompt) 
    print(f"\nInitial AI Response: {initial_response}")
    #get feedback and ratings
    rating=int(input("Rate from 1 (bad) to 5 (good): "))
    feedback=(input("Provide feedback for improvement: "))
    # Simulate model improvement based on feedback (in a real scenario, this feedback would be used to fine-tune the model)
    improved_response=(f"{initial_response} (Improved with your feedback:{feedback})")
    print(f"\nImproved AI Response: {improved_response}")
def role_based():
    #Conducts  the reinforcement learning activity.
    print("\n=== ROLE BASED ACTIVITY ===\n")
    #Get user input for roles and prompting
    category=input("Enter a category (e.g, science, history, math):')")
    item=input(f"Enter a specific {category} topic (e.g, photosynthesis for science):")
    #Generate responses for different roles
    teacher_prompt = f"You are a teacher. Explain {item} in simple terms."
    expert_prompt = f"You are an expert in {category}. Explain {item} in a detailed, technical manner."
    # Get AI responses for the different roles
    teacher_response = generate_response(teacher_prompt)
    expert_response = generate_response(expert_prompt)
    print(f"\n--- Teacher's Perspective ---\n{teacher_response}")
    print(f"\n--- Expert's Perspective ---\n{expert_response}")
def run_activity():
        #Runs the entire activity
        print("\n=== AI Learning Activity ===")
        #Choose sctivity
        activity_choice=input("which activity would you like to run? (1:reinforcement learning, 2: role-based prompts):")
        if activity_choice=="1":
            reinforcement_learning_activity()
        elif activity_choice=="2":
            role_based()
        else:
            print("Invalid choice. Please choose either 1 or 2")
if __name__=="__main__":
    run_activity()                
         