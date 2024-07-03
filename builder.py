from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """

    A interface do Builder especifica métodos para criar as diferentes partes do
    os objetos Produto.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    """

    As classes Concrete Builder seguem a interface do Builder e fornecem
    implementações específicas das etapas de construção. Seu programa pode ter
    diversas variações de Builders, implementadas de forma diferente.
    """

    def __init__(self) -> None:
        """
        Uma nova instância do construtor deve conter um objeto de produto em branco, que é
        usado em montagem posterior.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Os Construtores de Concreto devem fornecer seus próprios métodos para
        recuperando resultados. Isso ocorre porque vários tipos de construtores podem criar
        produtos totalmente diferentes que não seguem a mesma interface.
        Portanto, tais métodos não podem ser declarados na interface base do Builder
        (pelo menos em uma linguagem de programação de tipo estaticamente).

        Normalmente, após devolver o resultado final ao cliente, um construtor
        espera-se que a instância esteja pronta para começar a produzir outro produto.
        É por isso que é uma prática comum chamar o método reset no final do
        o corpo do método `getProduct`. No entanto, este comportamento não é obrigatório,
        e você pode fazer seus construtores esperarem por uma chamada de redefinição explícita do
        código do cliente antes de descartar o resultado anterior.
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Product1():
    """

    Faz sentido usar o padrão Builder somente quando seus produtos são bastante
    complexos e exigem configuração extensiva.

    Ao contrário de outros padrões de criação, diferentes construtores concretos podem produzir
    produtos não relacionados. Em outras palavras, os resultados de vários construtores podem não
    sempre siga a mesma interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """

    O Diretor é responsável apenas pela execução das etapas de construção em um
    sequência específica. É útil ao produzir produtos de acordo com um
    ordem ou configuração específica. A rigor, a classe Diretor é
    opcional, pois o cliente pode controlar os construtores diretamente.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        O Diretor funciona com qualquer instância do construtor que o código do cliente passa
        para isso. Desta forma, o código do cliente pode alterar o tipo final do novo
        produto montado.
        """
        self._builder = builder

    """

    O Diretor pode construir diversas variações do produto usando o mesmo
    etapas de construção
    """

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """

    O código do cliente cria um objeto construtor, passa-o para o diretor e então
    inicia o processo de construção. O resultado final é recuperado do
    objeto construtor.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Lembre-se de que o padrão Builder pode ser usado sem uma classe Director.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()