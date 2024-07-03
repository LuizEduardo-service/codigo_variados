"""As abstrações não devem depender de detalhes. Os detalhes devem depender de abstrações."""

from abc import ABC, abstractmethod

class FrontEnd:

    def __init__(self, database) -> None:
        self.data_base = database

    def mostrar_dados(self):
        dados = self.data_base.get_data()
        print(dados)


class Gerenciador(ABC):

    @abstractmethod
    def get_data(self):
        pass
    

class SqlServer(Gerenciador):

    def get_data(self):
        return 'Dados retornado do Sql Server'

class MongoDB(Gerenciador):

    def get_data(self):
        return 'Dados retornado do Mongo DB'
    

if __name__ == '__main__':

    front = FrontEnd(SqlServer())
    front.mostrar_dados()

    front2 = FrontEnd(MongoDB())
    front2.mostrar_dados()