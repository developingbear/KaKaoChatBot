from abc import *

class Command(metaclass=ABCMeta):
    
    @abstractmethod
    def run(self):
        pass
    @abstractmethod
    def getDescription(self):
        pass