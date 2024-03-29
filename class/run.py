from terrenos.quadrado import TerrenoQuadrado
from terrenos.retangular import TerrenoRetangular
from engenheiro import Engenheiro

# apos a aula de LSP

engenheiro = Engenheiro("Geraldo")
terrenoQuadrado = TerrenoQuadrado(4)
terrenoRetangular = TerrenoRetangular(2, 3)

engenheiro.medir_area(terrenoQuadrado)
engenheiro.medir_area(terrenoRetangular)