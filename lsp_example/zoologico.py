from typing import Type

class Animal:
    
    def comer(self):
        print("O Animal esta Comendo")

    def dormir(self):
        print("O Animal esta Dormindo")
        
    def andar(self):
        print("O Animal esta Andando na jaula")

class Aves(Animal):
    
    def __init__(self):
        super().__init__()

    def cantar(self):
        print("A Ave esta Cantando")

class Pinguim(Aves):
    
    def __init__(self):
        super().__init__()

    def escorregar(self):
        print("O Pinguim esta escorregando no gelo")
        
class Pessoa:
    
    def observar(self, animal: Type[Animal]):
        animal.comer()

roberto = Pessoa()
pinguim = Pinguim()
roberto.observar(pinguim)