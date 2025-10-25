import streamlit as st
from google import genai
from google.genai import types
import config
import io
#Initialize the Gemini API client
GEMINI_API_KEY = "AIzaSyBTecMs4bgUrkSD8yMPwJ76TtPQapC7Bmg"
client = genai.Client(api_key=GEMINI_API_KEY)
#Function to generate AI response from Gemini API
def generate_response(prompt:str, temperature:float=0.3)->str:
    """Generate a response from Gemini API."""
    try:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        config_params = types.GenerateContentConfig(temperature=temperature)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=contents, config=config_params)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
#Streamlit UI Setup
def setup_ui():
    st.title("AI teaching Assistant")    
    st.write("Welcome! You can ask me anything about various subjects, and I'll provide an answer.")
    if "history" not in st.session_state:
        st.session_state.history=[]
        #Buttons in a horizontal layout: Clear and Export
        col_clear, col_export=st.columns([1,2]) 
        with col_clear:
            if st.button("????Clear Conversation"):
                st.session_state.history=[]
                st.experimental_rerun()
        with col_export:
            if st.session_state.history:
                #Prepare conversation text for export
                export_text=""
                for idx, qa in enumerate(st.session_state.history, start=1):
                    expot_text+=f"Q{idx}:{qa['question']}\n"
                    expot_text+=f"A{idx}:{qa['answer']}\n"
                bio=io.BytesIO()
                bio.write(export_text.encode("utf-8"))
                bio.seek(0)
                st.downloads_button(
                    label="???? Export Chat History",
                    data=bio,
                    filename_name="AI_Teaching_Assistant_Conversation.txt",
                    mime="text/plain"
                )
                #User input
        user_input=st.text_input("Enter your question here:") 
        if st.button("Ask"):
            if user_input.strip():
                with st.spinner("Generating AI response..."):
                   response=generate_response(user_input.strip())
                st.session_state.history.append({"question":user_input.strip(),"answer":response})
            else:
                st.warning("Please entre a question before clicking ask")
        #Display conversation history
        st.markdown("### Conversation History")
        st.markdown(
           """
           <style>
           .history-box {
             max-height: 400px;
             overflow-y: auto;
             border: 1px solid #ddd;
             padding: 12px;
             background-color: #f9f9f9;
             border-radius: 6px;
             font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
             }
            .question {
             font-weight: 600;
             color: #0a6ebd;
             margin-top: 12px;
             margin-bottom: 4px;
             }
            .answer {
             margin-bottom: 16px;
             white-space: pre-wrap;
             color: #333;
             }
           </style>
           """,
           unsafe_allow_html=True,
        )
        history_html = '<div class="history-box">'
        for idx, qa in enumerate(st.session_state.history, start=1):
           q = qa["question"]
           a = qa["answer"]
           history_html += f'<div class="question">Q{idx}: {q}</div>'
           history_html += f'<div class="answer">A{idx}: {a}</div>'
        history_html += '</div>'
        st.markdown(history_html, unsafe_allow_html=True)
def main():
   setup_ui()
if __name__ == "__main__":
   main()               