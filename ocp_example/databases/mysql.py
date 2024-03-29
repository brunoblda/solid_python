class MysqlDB:
    def __init__(self):
        self.__conexao = "Mysql"
    
    def conectar(self) -> str:
        print("Conectando ao banco de dados Mysql")
        return self.__conexao
    
    def desconectar(self) -> None:
        print("Desconectando do banco de dados Mysql")