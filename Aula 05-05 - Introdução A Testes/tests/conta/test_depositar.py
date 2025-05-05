import pytest
import inspect

from conta import Conta


def test_quando_depositar_50_o_saldo_deve_ser_50():
    """
    Teste para quando for depositado o valor de 50, e
    for chamado o método get_saldo, o retorno esperado é 50.
    """
    saldo_esperado = 50

    conta_teste = Conta(
        nome="Conta Teste",
        data_nascimento="01/01/2000"
    )

    conta_teste.depositar(50)
    saldo = conta_teste.get_saldo()

    assert saldo_esperado == saldo


def test_se_o_deposito_for_negativo_deve_lancar_erro():
    """
    Quando passado um valor negativo para o método depositar,
    espera-se que seja lançado um erro com a seguinte descrição:
    O valor do depósito não pode ser negativo!
    """
    conta_teste = Conta(
        nome="Conta Teste",
        data_nascimento="01/01/2000"
    )

    with pytest.raises(ValueError, match="O valor do depósito não pode ser negativo!"):
        conta_teste.depositar(-100)


def test_se_o_deposito_for_0_deve_lancar_erro():
    """
    Quando passado um valor 0 para o método depositar,
    espera-se que seja lançado um erro com a seguinte descrição:
    O valor do depósito deve ser maior que 0!
    """
    conta_teste = Conta(
        nome="Conta Teste",
        data_nascimento="01/01/2000"
    )

    with pytest.raises(ValueError, match="O valor do depósito deve ser maior que 0!"):
        conta_teste.depositar(0)


def test_quando_deposito_recebe_string_deve_lancar_erro():
    """
    Quando passado um valor string para o método depositar,
    espera-se que seja lançado um erro com a seguinte descrição:
    O tipo do valor deve ser númérico!
    """
    conta_teste = Conta(
        nome="Conta Teste",
        data_nascimento="01/01/2000"
    )

    with pytest.raises(TypeError, match="O tipo do valor deve ser númérico!"):
        conta_teste.depositar("100")


def test_se_quantidade_de_parametros_e_igual_a_1():
    """
    Teste para verificar se a quantidade de parâmetros do método depositar
    é igual a 1.
    """
    conta_teste = Conta(
        nome="Conta Teste",
        data_nascimento="01/01/2000"
    )

    qtd_parametros = len(inspect.signature(conta_teste.depositar).parameters)
    assert qtd_parametros == 1


def test_se_parametro_da_funcao_depositar_se_chama_valor_deposito():
    """
    Teste para verificar o parâmetro esperado pelo método depositar
    se chama valor_deposito.
    """
    conta_teste = Conta(
        nome="Conta Teste",
        data_nascimento="01/01/2000"
    )

    parametros = inspect.signature(conta_teste.depositar).parameters
    assert list(parametros) == ["valor_deposito"]


def test_quando_valor_deposito_for_maior_que_1_000_000_000_deve_exibir_erro():
    """
    Testa se o valor do depósito é maior ou igual a 1_000_000_000 e exibe o seguinte
    erro caso verdade: O valor do depósito deve ser menor que 1_000_000_000
    """
    conta_teste = Conta(
        nome="Conta Teste",
        data_nascimento="01/01/2000"
    )

    with pytest.raises(ValueError, match="O valor do depósito deve ser menor que 1_000_000_000"):
        conta_teste.depositar(1_000_000_000)
