import requests
from transformers import AutoModel, AutoTokenizer

class OpensModels:
    def __init__(self):
        # Define a list of available open-source models
        self.available_models = [
            {"name": "OpenAI GPT-2", "model_id": "gpt2"},
            {"name": "OpenAI GPT-3", "model_id": "EleutherAI/gpt-neo-2.7B"},
            {"name": "Mixtral 8x7B", "model_id": "mistralai/Mixtral-8x7B-Instruct-v0.1"},
            
            # Add more models as needed
        ]

    def list_models(self):
        # Display the list of available open-source models
        for model in self.available_models:
            print(f"{model['name']} - Model ID: {model['model_id']}")

    def download_model(self, model_id):
        # Download the selected model files using Hugging Face Transformers
        model = AutoModel.from_pretrained(model_id)
        tokenizer = AutoTokenizer.from_pretrained(model_id)

        # You can further process or use the downloaded model as needed

# Example usage:
open_source_models = OpensModels()
open_source_models.list_models()

# Let's say the user selects "OpenAI GPT-3"
selected_model_id = "EleutherAI/gpt-neo-2.7B"
open_source_models.download_model(selected_model_id)