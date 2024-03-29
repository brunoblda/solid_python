from abc import ABC, abstractmethod

class Ave(ABC):
    @abstractmethod
    def comer(self):
        raise "Should Implement comer method" 
    
    @abstractmethod
    def voar(self):
        raise "Should Implement voar method"
    
    @abstractmethod
    def gritar(self):
        raise "Should Implement gritar method"

class AveVoadora(ABC):
    @abstractmethod
    def comer(self):
        raise "Should Implement comer method" 
    
    @abstractmethod
    def voar(self):
        raise "Should Implement voar method"
    
    @abstractmethod
    def gritar(self):
        raise "Should Implement gritar method"


class AveNaoVoadora(ABC):
    @abstractmethod
    def comer(self):
        raise "Should Implement comer method" 
    
    @abstractmethod
    def gritar(self):
        raise "Should Implement gritar method"
    