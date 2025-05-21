def get_valid_float(prompt: str) -> float:
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")