"""
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o 
em uma das seguintes categorias: 

*Criança (0-12 anos), 
*Adolescente (13-17 anos), 
*Adulto (18-59 anos) ou 
*Idoso (60 anos ou mais).

2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"

3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

4- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não. 
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
"""

def classificador_de_idade():
    try:
        idade = int(input("Digite sua idade: "))
        if 0 <= idade <= 12:
            print("Classificação: Criança")
        elif 13 <= idade <= 17:
            print("Classificação: Adolescente")
        elif 18 <= idade <= 59:
            print("Classificação: Adulto")
        elif idade >= 60:
            print("Classificação: Idoso")
        else:
            print("Idade inválida.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro para a idade.")

def calculadora_de_imc():
    try:
        peso = float(input("Digite seu peso (em kg): "))
        altura = float(input("Digite sua altura (em metros): "))
        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser valores positivos.")
            return
        
        imc = peso / (altura ** 2)
        print(f"Seu IMC é: {imc:.2f}")

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obeso"
        print(f"Classificação: {classificacao}")
    except ValueError:
        print("Entrada inválida. Por favor, digite números para peso e altura.")

def conversor_de_temperatura():
    try:
        temp = float(input("Digite a temperatura: "))
        origem = input("Unidade de origem (C, F, K): ").upper()
        destino = input("Unidade de destino (C, F, K): ").upper()

        if origem == destino:
            print(f"Temperatura convertida: {temp:.2f} {destino}")
            return

        resultado = None
        if origem == 'C':
            if destino == 'F':
                resultado = (temp * 9/5) + 32
            elif destino == 'K':
                resultado = temp + 273.15
        elif origem == 'F':
            if destino == 'C':
                resultado = (temp - 32) * 5/9
            elif destino == 'K':
                resultado = (temp - 32) * 5/9 + 273.15
        elif origem == 'K':
            if destino == 'C':
                resultado = temp - 273.15
            elif destino == 'F':
                resultado = (temp - 273.15) * 9/5 + 32
        
        if resultado is not None:
            print(f"Temperatura convertida: {resultado:.2f} {destino}")
        else:
            print("Unidades de temperatura inválidas ou combinação não suportada.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para a temperatura.")

def verificador_de_ano_bissexto():
    try:
        ano = int(input("Digite um ano: "))
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"O ano {ano} é bissexto.")
        else:
            print(f"O ano {ano} não é bissexto.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro para o ano.")


if __name__ == "__main__":
    while True:
        print("\nEscolha uma opção:")
        print("1- Classificador de Idade")
        print("2- Calculadora de IMC")
        print("3- Conversor de Temperatura")
        print("4- Verificador de Ano Bissexto")
        print("0- Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            classificador_de_idade()
        elif escolha == '2':
            calculadora_de_imc()
        elif escolha == '3':
            conversor_de_temperatura()
        elif escolha == '4':
            verificador_de_ano_bissexto()
        elif escolha == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
