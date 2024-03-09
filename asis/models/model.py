
models = {
    "Mistral 7B Instructv02": {"model_id": "Mistral-7B-Instruct-v0.2", "description": "", "type": "0","use":" OpenSource"},
    "Otro Modelo": {"model_id": "Otro-Modelo-v1.0", "description": "Descripción del modelo 2"},
    # Agrega más modelos según sea necesario
}

class Model:
    global models
    
    def __init__(self,modelName):
        self.modelName = modelName
        self.modelInfo = models.get(modelName)
        self.modelType = self.modelInfo["type"]
        
        print(self.modelInfo)
        
    def upload_model(self.modelInfo):
        if self.modelType:
            openmodels = OpenModels(self.modelInfo)
    


mymodel = Model("Mistral 7B Instructv02")
mymodel(Mistral7BInstructv02())
    
        