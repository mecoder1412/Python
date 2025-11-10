# ✨ Multi-Tool AI Web App ✨
# Created with Streamlit + Google Gemini + PIL (Python Imaging Library)
# Tools included: AI Teaching Assistant, Math Mastermind, Safe AI Image Generator

import streamlit as st
from google import genai
from google.genai import types
import config
import base64
from io import BytesIO
from PIL import Image
import datetime
import re

# ✅ Initialize Gemini API client
GEMINI_API_KEY = "AIzaSyAdD9PJRq_2R9RvEgQ3AE6cxbSV6vrHxIo"
client = genai.Client(api_key=config.GEMINI_API_KEY)

# ✅ Helper function to generate AI response
def generate_response(prompt: str, temperature: float = 0.3) -> str:
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt,
        generation_config=types.GenerationConfig(temperature=temperature)
    )
    return response.text

# 🧠 Streamlit app layout
st.set_page_config(page_title="AI Teaching Assistant", page_icon="🤖", layout="wide")
st.title("🤖 AI Teaching Assistant + Math Mastermind + Safe AI Image Generator")

# Sidebar navigation
tool = st.sidebar.selectbox("Choose a tool", ["AI Teaching Assistant", "Math Mastermind", "Safe AI Image Generator"])

# --- 🧑‍🏫 AI Teaching Assistant ---
if tool == "AI Teaching Assistant":
    st.header("🧑‍🏫 AI Teaching Assistant")
    st.markdown("Ask me any academic question or get help understanding a topic!")

    if "history_ata" not in st.session_state:
        st.session_state.history_ata = []

    # Text input for user question
    user_question = st.text_input("Enter your question:")

    if st.button("Get Answer"):
        if user_question.strip():
            ai_answer = generate_response(user_question)
            st.markdown(f"**You:** {user_question}")
            st.markdown(f"**AI:** {ai_answer}")
            st.session_state.history_ata.append((user_question, ai_answer))
        else:
            st.warning("Please enter a question before asking.")

    # Display conversation history
    if st.session_state.history_ata:
        st.subheader("🗂️ Conversation History")
        for i, (q, a) in enumerate(st.session_state.history_ata, 1):
            st.markdown(f"**{i}. You:** {q}")
            st.markdown(f"**AI:** {a}")

        col_clear, col_export = st.columns([1, 2])
        with col_clear:
            if st.button("🗑️ Clear History"):
                st.session_state.history_ata = []

        with col_export:
            export_text = "\n\n".join([f"You: {q}\nAI: {a}" for q, a in st.session_state.history_ata])
            st.download_button(
                label="💾 Export Chat History",
                data=export_text,
                file_name="AI_Teaching_Assistant_Conversation.txt",
                mime="text/plain"
            )

# --- 🔢 Math Mastermind ---
elif tool == "Math Mastermind":
    st.header("🔢 Math Mastermind")
    st.markdown("Solve math equations or get help with problems!")

    if "history_mm" not in st.session_state:
        st.session_state.history_mm = []

    math_problem = st.text_input("Enter a math problem (e.g., 2 + 2 * 3):")

    if st.button("Solve"):
        if math_problem.strip():
            try:
                solution = eval(math_problem)
                st.success(f"The answer is: **{solution}**")
                st.session_state.history_mm.append((math_problem, str(solution)))
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter a math problem first.")

    if st.session_state.history_mm:
        st.subheader("🗂️ Solved Problems")
        for i, (p, s) in enumerate(st.session_state.history_mm, 1):
            st.markdown(f"**{i}. Problem:** {p}")
            st.markdown(f"**Answer:** {s}")

        col_clear, col_export = st.columns([1, 2])
        with col_clear:
            if st.button("🗑️ Clear History"):
                st.session_state.history_mm = []

        with col_export:
            export_text = "\n\n".join([f"Problem: {p}\nAnswer: {s}" for p, s in st.session_state.history_mm])
            st.download_button(
                label="💾 Export Solved Problems",
                data=export_text,
                file_name="Math_Mastermind_Solutions.txt",
                mime="text/plain"
            )

# --- 🎨 Safe AI Image Generator ---
elif tool == "Safe AI Image Generator":
    st.header("🎨 Safe AI Image Generator")
    st.markdown("Generate fun and safe AI images using prompts!")

    image_prompt = st.text_area("Describe the image you want to generate:")
    safety_check = st.checkbox("✅ I confirm that my prompt follows safe and respectful guidelines.")

    forbidden_keywords = ["violence", "gore", "weapon", "blood", "nudity", "hate", "drugs"]
    pattern = re.compile("|".join(forbidden_keywords), re.IGNORECASE)

    if st.button("Generate Image"):
        if not image_prompt.strip():
            st.warning("Please describe the image first.")
        elif not safety_check:
            st.warning("Please confirm the safety checkbox before generating.")
        elif pattern.search(image_prompt):
            st.error("🚫 Your prompt contains unsafe or restricted words.")
        else:
            with st.spinner("Generating your image... please wait."):
                try:
                    response = client.models.generate_content(
                        model="gemini-1.5-flash",
                        contents=types.Content(
                            parts=[types.Part.from_text(image_prompt)],
                            role="user"
                        )
                    )
                    if response and response.candidates:
                        image_base64 = response.candidates[0].content.parts[0].inline_data.data
                        image_data = base64.b64decode(image_base64)
                        image = Image.open(BytesIO(image_data))
                        st.image(image, caption="Generated Image", use_container_width=True)

                        # Allow image download
                        buffer = BytesIO()
                        image.save(buffer, format="PNG")
                        st.download_button(
                            label="💾 Download Image",
                            data=buffer.getvalue(),
                            file_name=f"Generated_Image_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
                            mime="image/png"
                        )
                    else:
                        st.error("The AI didn't return an image. Try again with a clearer prompt.")
                except Exception as e:
                    st.error(f"⚠️ Error: {e}")
