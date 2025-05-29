import random
import string
import requests
from datetime import datetime

class PasswordGenerator:
    @staticmethod
    def generate(length=8):
        characters = string.ascii_letters + string.digits + "!@#$%&*"
        return ''.join(random.choice(characters) for _ in range(length))

class UserService:
    @staticmethod
    def get_random_user():
        url = "https://randomuser.me/api/"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()['results'][0]
            name = f"{data['name']['first']} {data['name']['last']}"
            email = data['email']
            country = data['location']['country']
            return f"Nome: {name}\nEmail: {email}\nPaís: {country}"
        except requests.RequestException as e:
            return f"Erro ao obter usuário aleatório: {e}"

class AddressService:
    @staticmethod
    def get_address_by_cep(cep):
        url = f"https://viacep.com.br/ws/{cep}/json/"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if "erro" in data:
                return "CEP não encontrado."
            return f"""CEP: {data['cep']}
Logradouro: {data['logradouro']}
Bairro: {data['bairro']}
Cidade: {data['localidade']}
Estado: {data['uf']}"""
        except requests.RequestException as e:
            return f"Erro na consulta: {e}"

class CurrencyService:
    @staticmethod
    def get_exchange_rate(currency):
        url = f"https://economia.awesomeapi.com.br/last/{currency}-BRL"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            rate = data[f"{currency}BRL"]
            return f"""Moeda: {currency} para BRL
Valor: R$ {float(rate['bid']):.2f}
Máxima: R$ {float(rate['high']):.2f}
Mínima: R$ {float(rate['low']):.2f}
Data/Hora: {datetime.fromtimestamp(int(rate['timestamp']))}"""
        except requests.RequestException as e:
            return f"Erro ao obter cotação: {e}"
        except KeyError:
            return "Moeda não encontrada ou não suportada."

class MenuController:
    def __init__(self):
        self.password_generator = PasswordGenerator()
        self.user_service = UserService()
        self.address_service = AddressService()
        self.currency_service = CurrencyService()

    def display_menu(self):
        print("\n=== MENU PRINCIPAL ===")
        print("1. Gerar senha aleatória")
        print("2. Obter usuário aleatório")
        print("3. Consultar CEP")
        print("4. Consultar cotação de moeda")
        print("5. Sair")
        print("=" * 22)

    def handle_password_generation(self):
        try:
            length = int(input("Digite o tamanho da senha desejada: "))
            if length <= 0:
                print("Tamanho deve ser maior que zero.")
                return
            password = self.password_generator.generate(length)
            print(f"Sua senha gerada é: {password}")
        except ValueError:
            print("Por favor, digite um número válido.")

    def handle_random_user(self):
        print("Gerando um usuário aleatório...")
        user = self.user_service.get_random_user()
        print(user)

    def handle_cep_lookup(self):
        cep = input("Digite um CEP para consulta (apenas números): ")
        if not cep.isdigit() or len(cep) != 8:
            print("CEP deve conter exatamente 8 dígitos.")
            return
        print("\nConsultando CEP...")
        result = self.address_service.get_address_by_cep(cep)
        print(result)

    def handle_currency_rate(self):
        currency = input("Digite o código da moeda para cotação (ex: USD, EUR, GBP): ").upper()
        if not currency.isalpha() or len(currency) != 3:
            print("Código da moeda deve ter 3 letras.")
            return
        print("\nObtendo cotação...")
        result = self.currency_service.get_exchange_rate(currency)
        print(result)

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = input("Escolha uma opção (1-5): ").strip()
                
                if choice == "1":
                    self.handle_password_generation()
                elif choice == "2":
                    self.handle_random_user()
                elif choice == "3":
                    self.handle_cep_lookup()
                elif choice == "4":
                    self.handle_currency_rate()
                elif choice == "5":
                    print("Saindo...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except KeyboardInterrupt:
                print("\nSaindo...")
                break
            except Exception as e:
                print(f"Erro inesperado: {e}")

def main():
    controller = MenuController()
    controller.run()

if __name__ == "__main__":
    main()