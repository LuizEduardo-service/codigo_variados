from abc import ABC, abstractmethod
from .open_erro import TipoExame

class AprovarExame(ABC):

    @abstractmethod
    def aprovar_solicitacao_exame(exame: TipoExame):
        pass

    @abstractmethod
    def verificar_condicoes_exame(exame: TipoExame):
        pass


class SolicitacaoExameSangue(AprovarExame):

    def aprovar_solicitacao_exame(self, exame: TipoExame):
        if self.verificar_condicoes_exame(exame):
            print('Exame Aprovado')
    
    def verificar_condicoes_exame(self, exame: TipoExame):
        print(f'verificando Exame de {exame.tipo}')
        return True
    
class SolicitacaoExameRaioX(AprovarExame):

    def aprovar_solicitacao_exame(self, exame: TipoExame):
        if self.verificar_condicoes_exame(exame):
            print('Exame Aprovado')
    
    def verificar_condicoes_exame(self, exame: TipoExame):
        print(f'verificando Exame de {exame.tipo}')
        return True
    