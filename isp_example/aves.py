from interface import Ave 

class Canario(Ave):

    def comer(self):
        print("Estou comendo!")

    def voar(self):
        print("Estou voando!")
        
    def gritar(self):
        print("Estou gritando!")

class Pinguim(Ave):
    
    def comer(self):
        print("Estou comendo!")
        self.__acasalar()
    
    # o principio ISP diz que uma classe não deve ser forçada a implementar métodos que não serão utilizados    
    def voar(self):
        None
    
    def gritar(self):
        print("Estou gritando!")
        
    def __acasalar(self):
        print("Agora vou acasalar ...")