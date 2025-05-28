import datetime

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round(gorjeta, 2)


def is_palindromo(texto):
    texto_limpo = ''.join(char.lower() 
                          for char in texto 
                          if char.isalnum())
    return texto_limpo == texto_limpo[::-1]

def calcular_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return round(preco_final, 2)

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

def obter_valor_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0:
                return valor
            print("Por favor, digite um valor positivo.")
        except ValueError:
            print("Por favor, digite um número válido.")

def obter_ano_valido():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento: "))
            ano_atual = datetime.datetime.now().year
            if 1900 <= ano <= ano_atual:
                return ano
            print(f"Por favor, digite um ano entre 1900 e {ano_atual}.")
        except ValueError:
            print("Por favor, digite um ano válido.")

def obter_texto():
    while True:
        texto = input("Digite o texto para verificar: ").strip()
        if texto:
            return texto
        print("Por favor, digite um texto válido.")

def executar_calculadora_gorjeta():
    print("\n=== CALCULADORA DE GORJETA ===")
    valor_conta = obter_valor_positivo("Digite o valor da conta: R$ ")
    porcentagem = obter_valor_positivo("Digite a porcentagem de gorjeta: ")
    
    gorjeta = calcular_gorjeta(valor_conta, porcentagem)
    valor_total = valor_conta + gorjeta
    
    print(f"\nValor da conta: R$ {valor_conta:.2f}")
    print(f"Gorjeta ({porcentagem}%): R$ {gorjeta:.2f}")
    print(f"Total a pagar: R$ {valor_total:.2f}")

def executar_verificador_palindromo():
    print("\n=== VERIFICADOR DE PALÍNDROMO ===")
    texto = obter_texto()
    
    resultado = is_palindromo(texto)
    resposta = "Sim" if resultado else "Não"
    
    print(f"'{texto}' é um palíndromo? {resposta}")

def executar_calculadora_desconto():
    print("\n=== CALCULADORA DE DESCONTO ===")
    preco_original = obter_valor_positivo("Digite o preço do produto: R$ ")
    desconto = obter_valor_positivo("Digite o percentual de desconto: ")
    
    preco_final = calcular_desconto(preco_original, desconto)
    valor_desconto = preco_original - preco_final
    
    print(f"\nPreço original: R$ {preco_original:.2f}")
    print(f"Desconto ({desconto}%): R$ {valor_desconto:.2f}")
    print(f"Preço final: R$ {preco_final:.2f}")

def executar_calculadora_idade():
    print("\n=== CALCULADORA DE IDADE EM DIAS ===")
    ano_nascimento = obter_ano_valido()
    
    idade_em_dias = calcular_idade_em_dias(ano_nascimento)
    idade_em_anos = datetime.datetime.now().year - ano_nascimento
    
    print(f"\nIdade em anos: {idade_em_anos}")
    print(f"Idade aproximada em dias: {idade_em_dias} dias")

def exibir_menu():
    print("\n" + "="*50)
    print("           MENU PRINCIPAL")
    print("="*50)
    print("1. Calculadora de Gorjeta")
    print("2. Verificador de Palíndromo")
    print("3. Calculadora de Desconto")
    print("4. Calculadora de Idade em Dias")
    print("5. Sair")
    print("="*50)

def obter_opcao_menu():
    while True:
        try:
            opcao = int(input("Escolha uma opção (1-5): "))
            if 1 <= opcao <= 5:
                return opcao
            print("Por favor, escolha uma opção entre 1 e 5.")
        except ValueError:
            print("Por favor, digite um número válido.")

def executar_aplicacao():
    print("Bem-vindo ao Sistema de Utilidades!")
    
    while True:
        exibir_menu()
        opcao = obter_opcao_menu()
        
        if opcao == 1:
            executar_calculadora_gorjeta()
        elif opcao == 2:
            executar_verificador_palindromo()
        elif opcao == 3:
            executar_calculadora_desconto()
        elif opcao == 4:
            executar_calculadora_idade()
        elif opcao == 5:
            print("\nObrigado por usar o sistema!")
            break
        
        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    executar_aplicacao()
