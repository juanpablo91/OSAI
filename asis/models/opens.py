import requests
from transformers import AutoModel, AutoTokenizer


from ASIS.models import available_models

loaded_models = {}

def load_model(model_name):
    if model_name not in loaded_models:
        module = __import__(f"asis.models.{model_name}", fromlist=[""])
        config_module = __import__(f"asis.config.{model_name}_config", fromlist=[""])
        # Puedes inicializar el modelo con la configuración si es necesario
        model_instance = module.Model(config_module.config)
        loaded_models[model_name] = model_instance
    return loaded_models[model_name] 

from uploadmodel import UploadModel

class OpensModels():
    def __init__(self,model_info):
        self.model_info = model_info
        
    uploader = (self.model_info["model_id"]+"()")
    
    
