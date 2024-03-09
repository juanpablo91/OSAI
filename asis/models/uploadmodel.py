


from abc import abc, abstractclassmethod

class UploadModel(ABC):
    @abstractmethod
    def upload(self,nameModel):
        pass
    
