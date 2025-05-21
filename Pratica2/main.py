"""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""

def conversor_moeda():
    print("--- Conversor de Moeda ---")
    try:
        valor_reais = float(input("Digite o valor em Reais (R$): "))
        taxa_dolar = float(input("Digite a taxa do Dólar: "))
        taxa_euro = float(input("Digite a taxa do Euro: "))

        valor_dolares = round(valor_reais / taxa_dolar, 2)
        valor_euros = round(valor_reais / taxa_euro, 2)

        print(f"Valor em Reais: R$ {valor_reais:.2f}")
        print(f"Valor em Dólares: $ {valor_dolares:.2f}")
        print(f"Valor em Euros: € {valor_euros:.2f}")
    except ValueError:
        print("Entrada inválida. Por favor, digite números.")
    print("\n")

def calculadora_desconto():
    print("--- Calculadora de Desconto ---")
    try:
        nome_produto = input("Digite o nome do produto: ")
        preco_original = float(input("Digite o preço original (R$): "))
        percentual_desconto = float(input("Digite o percentual de desconto (%): "))

        if not (0 <= percentual_desconto <= 100):
            print("Percentual de desconto inválido. Deve ser entre 0 e 100.")
            return

        valor_desconto = (preco_original * percentual_desconto) / 100
        preco_final = preco_original - valor_desconto

        print(f"Produto: {nome_produto}")
        print(f"Preço Original: R$ {preco_original:.2f}")
        print(f"Desconto: {percentual_desconto}%")
        print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
        print(f"Preço Final: R$ {preco_final:.2f}")
    except ValueError:
        print("Entrada inválida. Por favor, digite números para preço e desconto.")
    print("\n")

def calculadora_media_escolar():
    print("--- Calculadora de Média Escolar ---")
    try:
        nota1 = float(input("Digite a Nota 1: "))
        nota2 = float(input("Digite a Nota 2: "))
        nota3 = float(input("Digite a Nota 3: "))

        media_escolar = round((nota1 + nota2 + nota3) / 3, 2)

        print(f"Nota 1: {nota1:.1f}")
        print(f"Nota 2: {nota2:.1f}")
        print(f"Nota 3: {nota3:.1f}")
        print(f"Média Final: {media_escolar:.2f}")
    except ValueError:
        print("Entrada inválida. Por favor, digite números para as notas.")
    print("\n")

def calculadora_consumo_combustivel():
    print("--- Calculadora de Consumo de Combustível ---")
    try:
        distancia_percorrida = float(input("Digite a distância percorrida (km): "))
        combustivel_gasto = float(input("Digite o combustível gasto (litros): "))

        if combustivel_gasto <= 0:
            print("Consumo de combustível deve ser maior que zero.")
            return

        consumo_medio = round(distancia_percorrida / combustivel_gasto, 2)

        print(f"Distância percorrida: {distancia_percorrida} km")
        print(f"Combustível gasto: {combustivel_gasto} litros")
        print(f"Consumo médio: {consumo_medio:.2f} km/l")
    except ValueError:
        print("Entrada inválida. Por favor, digite números para distância e combustível.")
    print("\n")

if __name__ == "__main__":
    conversor_moeda()
    calculadora_desconto()
    calculadora_media_escolar()
    calculadora_consumo_combustivel()
  