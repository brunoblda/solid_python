class SistemaCadastral:
    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__indicar_error()
            
    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        return False

    def __armazenar_usuario(self, nome: str, idade: int) -> None:
        print("acessando o banco de dados...")
        print("Cadastrar o Usuario {}, Idade {}".format(nome, idade))

    def __indicar_error(self) -> None:
        print("dados invalidos!")

class VerificardorDeDados:
    pass