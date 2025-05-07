class Aluno:

    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__notas = []

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def notas(self):
        return self.__notas

    @property
    def media(self):
        return round(sum(self.__notas) / len(self.__notas), 2)

    @nome.setter
    def nome(self, nome):
        if nome is None or nome.strip() == "":
            raise ValueError("O nome do aluno não pode ser vazio")
        self.__nome = nome

    @idade.setter
    def idade(self, idade):
        if idade <= 0:
            raise ValueError("A idade deve ser um número positivo")
        self.__idade = idade

    def adicionar_nota(self, nota):
        if not isinstance(nota, (int, float)):
            raise TypeError("A nota deve ser um número")

        self.__notas.append(nota)

    def verificar_aprovacao(self):
        return self.media >= 6
