from random import randint
import inspect


class Conta:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.saldo = 0
        self.nr_conta = randint(10000, 99999)

    def depositar(self, valor_deposito):
        """
        Este método tem como objetivo incrementar o valor enviado em
        valor_deposito na variável saldo.

        Args:
            valor_deposito: Float | Int

        Returns:
            None
        """

        if not isinstance(valor_deposito, (int, float)):
            raise TypeError("O tipo do valor deve ser númérico!")

        if valor_deposito < 0:
            raise ValueError("O valor do depósito não pode ser negativo!")

        if valor_deposito == 0:
            raise ValueError("O valor do depósito deve ser maior que 0!")

        if valor_deposito >= 1_000_000_000:
            raise ValueError("O valor do depósito deve ser menor que 1_000_000_000")

        self.saldo += valor_deposito

    def sacar(self, valor_saque):

        if not isinstance(valor_saque, (int, float)):
            raise TypeError("O valor de saque deve ser numérico!")

        if isinstance(valor_saque, float) and len(str(valor_saque).split('.')[-1]) != 2:
            raise ValueError('O valor_saque deve possuir duas casas decimais')

        if valor_saque <= 0:
            raise ValueError("O valor de saque deve ser maior que 0!")

        if valor_saque > self.saldo:
            raise ValueError('O valor de saque deve ser maior ou igual ao saldo')

        self.saldo -= valor_saque

    def get_saldo(self):
        return self.saldo
