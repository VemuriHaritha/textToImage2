import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Streamlit title 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
st.title('Text-to-Image Generator using Stable Diffusion API')

# Text prompt input
prompt = st.text_input("Enter a text prompt:", value="A serene beach at sunset")

# Generate button
if st.button("Generate Image"):
    # API URL for Stable Diffusion (Hugging Face)
    API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"

    # Set up headers
    headers = {
        "Authorization": "Bearer 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"  # Use your Hugging Face API key if necessary
    }

    # Data for the request
    data = {
        "inputs": prompt
    }

    # Send request to the Hugging Face API
    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        # Get the image data from the response
        image_data = response.content  # This contains the raw image data

        # Open the image using PIL
        img = Image.open(BytesIO(image_data))

        # Display the generated image in Streamlit
        st.image(img, caption=f"Generated image for: {prompt}", use_column_width=True)
    else:
        st.error(f"Failed to generate image: {response.text}")
