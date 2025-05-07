import pytest
from conta import Conta


def test_quando_nao_for_enviado_valor_numerico_deve_ocorrer_erro():
    conta_teste = Conta(
        nome="Teste",
        data_nascimento="01/01/2000"
    )

    with pytest.raises(TypeError, match='O valor de saque deve ser numérico!'):
        conta_teste.sacar('100')


def test_se_o_valor_do_saque_eh_igual_a_zero_deve_lancar_erro():
    conta_teste = Conta(
        nome="Teste",
        data_nascimento="01/01/2000"
    )

    with pytest.raises(ValueError, match='O valor de saque deve ser maior que 0!'):
        conta_teste.sacar(0)


def test_se_o_valor_do_saque_eh_menor_que_zero_deve_lancar_erro():
    conta_teste = Conta(
        nome="Teste",
        data_nascimento="01/01/2000"
    )

    with pytest.raises(ValueError, match='O valor de saque deve ser maior que 0!'):
        conta_teste.sacar(-1)


def test_se_o_valor_do_saque_eh_maior_ou_igual_ao_saldo_deve_realizar_saque():
    conta_teste = Conta(
        nome="Teste",
        data_nascimento="01/01/2000"
    )

    conta_teste.depositar(100)
    conta_teste.sacar(100)

    assert conta_teste.saldo == 0


def test_se_o_valor_do_saque_eh_menor_que_o_saldo_deve_lancar_erro():
    conta_teste = Conta(
        nome="Teste",
        data_nascimento="01/01/2000"
    )

    conta_teste.depositar(100)

    with pytest.raises(ValueError, match='O valor de saque deve ser maior ou igual ao saldo'):
        conta_teste.sacar(100.01)


def test_se_o_valor_do_saque_tiver_mais_que_duas_casas_decimais_deve_lancar_erro():
    conta_teste = Conta(
        nome="Teste",
        data_nascimento="01/01/2000"
    )

    with pytest.raises(ValueError, match='O valor_saque deve possuir duas casas decimais'):
        conta_teste.sacar(100.001)

# def test_se_o_saldo_eh_calculado_corretamente_apos_varias_operacoes_de_saque_e_deposito():
#     depositos = [100, 200, 300, 400, 500, 600, 700, 800, 900,
#                  10, 20, 30, 40, 50, 60, 70, 80, 90,
#                  10.10, 20.20, 30.30, 40.40, 50.50, 60.60, 70.70, 80.80, 90.0]
