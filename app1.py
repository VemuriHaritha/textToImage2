import streamlit as st
import requests
from PIL import Image
from io import BytesIO
st.title('Text-to-Image Generator using Stable Diffusion API by Haritha V')
prompt = st.text_input("Enter a text prompt:", value="A serene beach at sunset")
if st.button("Generate Image"):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {
        "Authorization": "Bearer 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"  
    }
    data = {
        "inputs": prompt
    }
    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        image_data = response.content  
        img = Image.open(BytesIO(image_data))
        st.image(img, caption=f"Generated image for: {prompt}", use_column_width=True)
    else:
        st.error(f"Failed to generate image: {response}")
    response = requests.post(API_URL, headers=headers, json=data)
