from typing import Type

class Conexao:
    
    def conectar(self) -> None:
        print("Connectando ao banco de dados")

    def desconectar(Self) -> None:
        print("Desconectando ao banco de dados")

class MysqlRepo(Conexao):
   
    def __init__(self):
        super().__init__()

    def select(self):
        self.conectar()
        print("SELECT * FROM table")

    
class CasoDeUso:
    
    def buscar(self, db_repo: Type[MysqlRepo]):
        db_repo.select()