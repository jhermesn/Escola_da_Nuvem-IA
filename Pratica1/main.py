from functions.saudacao import saudacao
from functions.soma import soma
from functions.calcularParalelepipedo import calcularParalelepipedo
from functions.precoTotal import calcularPrecoTotal

from validations.valid_int import get_valid_int
from validations.valid_float import get_valid_float
from validations.valid_name import get_valid_nome

if __name__ == "__main__":
    while True:
        print("1 - Saudação")
        print("2 - Soma")
        print("3 - Paralelepipedo")
        print("4 - Preço Total")
        print("5 - Sair")
        opcao = get_valid_int("Digite a opção: ")

        match opcao:
            case 1:
                nome = get_valid_nome("Digite seu nome: ")
                print(saudacao(nome))
                print("\n")
            case 2:
                a = get_valid_int("Digite o valor do lado 1: ")
                b = get_valid_int("Digite o valor do lado 2: ")
                print(soma(a, b))
                print("\n")
            case 3:
                a = get_valid_int("Digite o valor do lado 1: ")
                b = get_valid_int("Digite o valor do lado 2: ")
                c = get_valid_int("Digite o valor do lado 3: ")
                print(calcularParalelepipedo(a, b, c))
                print("\n")
            case 4:
                valor = get_valid_float("Digite o valor do produto: ")
                quantidade = get_valid_int("Digite a quantidade do produto: ")
                print(calcularPrecoTotal(valor, quantidade))
                print("\n")
            case 5:
                break
            case _:
                print("Opção inválida")
                print("\n")