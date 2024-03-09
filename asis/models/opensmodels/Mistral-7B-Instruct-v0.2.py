
from transformers import AutoModelForCausalLM, AutoTokenizer
from uploadmodel import UploadModel




class Mistral7BInstructv02(UploadModel):
    def upload(self, modelName):
        model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
        tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
        return model
    