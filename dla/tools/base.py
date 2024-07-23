from abc import ABC, abstractmethod

class BaseAgent(ABC): 

    @abstractmethod
    def set_model(self): 
        pass

    @abstractmethod
    def get_model(self): 
        ...

    @abstractmethod
    def detect(self, image): 
        ...