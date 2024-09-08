# Author - Rayan Hussain

import os
import gradio as gr
from dotenv import load_dotenv
from langchain import HuggingFaceHub
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from huggingface_hub import login

# import sys
# # print(sys.executable)

# Load environment variables from the .env file
load_dotenv()

# Get the Hugging Face API token from environment variables
hf_api_token = os.getenv('HUGGINGFACE_TOKEN')
# print(hf_api_token)

# Log in to Hugging Face with the API token
login(hf_api_token)

# Define the translation model
hf_model = "Helsinki-NLP/opus-mt-en-fr"

# Initialise the Hugging Face translation model with specific settings
translator_model = HuggingFaceHub(huggingfacehub_api_token=hf_api_token, 
                                  repo_id=hf_model,
                                  model_kwargs={"temperature":0.8, "max_new_tokens":200})

# Simple prompt template for the model input
template = """
{query}
"""
# Define a prompt object to prepare input before passing to the model
prompt = PromptTemplate(template=template, input_variables=["query"])        

# Create a chain that connects the prompt to the translator model
translation_chain = prompt | translator_model

# TESTING :
# try:
#     result = translation_chain.invoke({"query": "Hello there friend"})
#     print(result)
# except Exception as e:
#     print(f"Error: {e}")

# Define the translation function
def translate_text(query):
    try:
        # Translate the input query
        result = translation_chain.invoke({"query": query})
        return result
    except Exception as e:
        return f"Error: {e}"

# Set up the Gradio interface with input and output boxes
iface = gr.Interface(
    fn=translate_text, 
    inputs=gr.Textbox(lines=2, placeholder="Type English text here...", label="English"),
    outputs=gr.Textbox(lines=2, placeholder="Translated French text will appear here...", label="French"),
    title="Rayan's English to French Translator",
    description="Type your text to translate from English to French."
)

# If the script is run directly, launch the Gradio interface
if __name__ == "__main__":
    iface.launch()
