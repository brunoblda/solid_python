# Quebra do principio de substituição de Liskov
# O principio de substituição de Liskov diz que uma classe derivada deve ser substituível por sua classe base sem quebrar o comportamento do programa.

class PessoaA:
    def se_apresentar(self):
        print("Ola, sou a pessoa A")


class PessoaB(PessoaA):
    def __init__(self):
        super().__init__()

    def se_apresentar(self):
        print("Estou alterando esse método")


pessoa = PessoaA()
pessoa.se_apresentar()

pessoa2 = PessoaB()
pessoa2.se_apresentar()