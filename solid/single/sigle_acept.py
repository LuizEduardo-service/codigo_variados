
"""
o princípio da responsabilidade única diz que: “Cada classe deve ter um, e somente um, motivo para mudar.”
Se uma classe tem várias responsabilidades, 
mudar um requisito do projeto pode trazer várias razões para modificar a classe. Por isso, as classes devem ter responsabilidades únicas.
"""

class GerenciarTarefas:

    def criarTarefa(self):
        pass

    def atualizarTarefa(self):
        pass

    def removerTarefa(self):
        pass

class GerenciarAPI:

    def conectarAPI(self):
        pass

class EnviarNotificacao:

    def enviarNotificacao(self):
        pass

class GerenciarRelatorio:

    def produzirRelatorio(self):
        pass

    def enviarRelatorio(self):
        pass
    