class Circo:
    # classe fechada
    def apresentar(self, tipo):
        if tipo == 1:
            self.apresentar_malabarista()
        if tipo == 2:
            self.apresentar_palhaco()
        
    def apresentar_malabarista(self):
        print("Malabarista apresentando seu show")

    def apresentar_palhaco(self):
        print("Palhaço apresentando seu show")


class Circo2:
    # classe aberta para extensoes, mas fechada para alteracoes
    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()
    
class Malabarista:
    def apresentar_show(self):
        print("Malabarista apresentando seu show")
        
class Palhaco:
    def apresentar_show(self):
        print("Palhaço apresentando seu show")
        
class Domador:
    def apresentar_show(self):
        print("Domador apresentando seu show")

circo = Circo()