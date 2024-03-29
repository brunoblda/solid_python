from typing import Type
from interfaces.formas import FormasInterface

class Engenheiro:
    
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def medir_perimetro(self, terreno: Type[FormasInterface]) -> None:
        perimetro = terreno.get_perimetro()
        print("{} mediu o perimentro: {} m".format(self.nome, perimetro))

    def medir_area(self, terreno: Type[FormasInterface]) -> None:
        area = terreno.get_area()
        print("{} mediu a area: {} m2".format(self.nome, area))