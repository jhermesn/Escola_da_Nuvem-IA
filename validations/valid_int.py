def get_valid_int(prompt: str) -> int:
    while True:
        value = input(prompt)
        if value.strip().isdigit():
            return int(value)
        print("Entrada inválida. Por favor, digite um número inteiro válido.")