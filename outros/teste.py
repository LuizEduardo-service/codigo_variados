
from typing import Type



class Livros:

    def __init__(self, titulo, autor, data_lancamento) -> None:
        self.titulo = titulo
        self.autor = autor
        self.data_lancamento = data_lancamento



class ImprimirLivro:

    def __init__(self, livro: Type[Livros]) -> None:
        self.livro = livro

    def imprimir_livro(self):
        return f'\nTitulo:{self.livro.titulo}\nAutor: {self.livro.autor}\nData: {self.livro.data_lancamento}'
    

if __name__ == '__main__':
    l = Livros("Minhas Memorias", "Luiz Eduardo", "15/04/2024")      
    imp = ImprimirLivro(l)
    print(imp.imprimir_livro())
