# Author - Rayan Hussain

import sys
import os
import requests
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
import gradio as gr

# Load environment variables from the .env file
load_dotenv()

# Get the Hugging Face API token from environment variables
hf_api_token = os.getenv('HUGGINGFACE_TOKEN')
# print(hf_api_token)

# Define the model ID and the API endpoint URL for Hugging Face's API
hf_model = "CompVis/stable-diffusion-v1-4"
endpoint_url = f"https://api-inference.huggingface.co/models/{hf_model}"

# Set up the headers for the API request, including the API token
headers = {
    "Authorization": f"Bearer {hf_api_token}",
    "Content-Type": "application/json"
}

# Define the function to generate an image from a text prompt
def generate_image(prompt):
    # Send a POST request to the Hugging Face API with the prompt
    response = requests.post(endpoint_url, headers=headers, json={"inputs": prompt})
    
    # If the request is successful (status code 200), process the image
    if response.status_code == 200:
        # Convert the binary response content into an image
        image = Image.open(BytesIO(response.content))
        # image.save("generated_image.png")
        # Display the generated image
        image.show()  
        # print("Image generated and saved as 'generated_image.png'")
        return image
    # Print the error if the request fails
    else:
        print(f"Error: {response.status_code} - {response.text}")

# TESTING :
# try:
#     generate_image("tree")
# except Exception as e:
#     print(f"Error: {e}")

# Set up the Gradio interface with input and output boxes
iface = gr.Interface(
    fn=generate_image, 
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here...", label="Prompt"),
    outputs=gr.Image(type="pil", label="Generated Image"),
    title="Rayan's AI Image Generator",
    description="Enter a prompt to generate an image!"
)

# If the script is run directly, launch the Gradio interface
if __name__ == "__main__":
    iface.launch()