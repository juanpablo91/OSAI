import requests
from transformers import AutoModel, AutoTokenizer


from ASIS.models import available_models

loaded_models = {}



from uploadmodel import UploadModel

class OpensModels():
    global loaded_models
    def __init__(self,model_info):
        self.model_info = model_info
        
        

    global loaded_models = {}

    def import_model(model_name):
        if model_name not in loaded_models:
            module = __import__(f"ASIS.models.{model_name}", fromlist=[""])
            loaded_models[model_name] = module
        return loaded_models[model_name]

    
    
