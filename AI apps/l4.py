import streamlit as st
from google import genai
from google.genai import types
import config
import base64
from io import BytesIO
from PIL import Image

GEMINI_API_KEY = "AIzaSyDIPfOAdHsXBT5I1HVsDWodcL-syL5YNco"

# Initialize Gemini API client
# ✅ Use the correct key source — pick one method
client = genai.Client(api_key=GEMINI_API_KEY)  # or use config.GEMINI_API_KEY if you have it in config.py

# Function to generate AI response from Gemini API
def generate_image(prompt, model="gemini-2.5-flash-image", size="1024x1024", temperature=0.8):
    """Generate a response from Gemini API."""
    try:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        config_params = types.GenerateContentConfig(
            temperature=temperature,
            candidate_count=1,
            max_output_tokens=2048
        )

        response = client.models.generate_content(
            model=model, contents=contents, config=config_params
        )

        # Check for image data
        for chunk in response.candidates[0].content.parts:
            if hasattr(chunk, "inline_data") and chunk.inline_data and chunk.inline_data.mime_type.startswith("image/"):
                inline_data = chunk.inline_data.data
                image_bytes = base64.b64decode(inline_data)
                image = Image.open(BytesIO(image_bytes))
                return image, None  # ✅ Always return a tuple (image, error)

        return None, "No image was generated in the response."
    except Exception as e:
        return None, f"Error during image generation: {str(e)}"  # ✅ Added colon after message


# Streamlit UI
def main():
    st.set_page_config(page_title="AI Image Generator", layout="centered")
    st.title("🎨 AI Image Generator")
    st.write("Enter a description to generate a safe and responsible AI image using Gemini 2.0 Flash.")
    st.write("Examples: *A serene sunset over a mountain lake*, *A futuristic city skyline at night*")

    # Info about model
    st.info("⚡ This app uses Gemini 2.0 Flash Preview for image generation with streaming responses.")

    # Input
    prompt = st.text_area(
        "Image Description",
        help="Describe the image you want to generate. Be specific for better results."
    )
    submit = st.button("Generate Image")

    if submit:
        if not prompt.strip():
            st.warning("Please enter an image description.")
        else:
            with st.spinner("Generating image... This may take a few moments."):  # ✅ grammar fix
                image, error = generate_image(prompt)

            if image:
                st.image(image, caption="Generated Image", use_container_width=True)
                # Save in session state for download
                st.session_state.generated_image = image  # ✅ renamed to avoid confusion
            else:
                st.error(error or "Failed to generate image. Please try again with a different prompt.")

    # Download button if image exists
    if "generated_image" in st.session_state:  # ✅ updated session key
        buf = BytesIO()
        st.session_state.generated_image.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.download_button(
            label="Download Generated Image",
            data=byte_im,
            file_name="generated_image.png",
            mime="image/png"
        )


if __name__ == "__main__":
    main()
