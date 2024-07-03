from dataclasses import dataclass


@dataclass
class TipoExame:
    tipo: str


class AprovarExame:

    def __init__(self, exame: TipoExame):
        self.exame = exame

    def verificarExame(self):
        if self.exame.tipo == "SANGUE":
            self.executarExameSangue()

        elif self.exame.tipo == "RaioX":
            self.executarExameRaioX()

    def executarExameSangue(self):
        print(f'Exame de {self.exame.tipo} Aprovado')

    def executarExameRaioX(self):
        print(f'Exame de {self.exame.tipo} Aprovado')



if __name__ == '__main__':

    exame = TipoExame(tipo="SANGUE")
    aprovar_exame = AprovarExame(exame)
    aprovar_exame.verificarExame()