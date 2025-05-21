def get_valid_nome(prompt: str) -> str:
    while True:
        value = input(prompt)
        if value.strip():
            return value.strip()
        print("Entrada inválida. Por favor, digite um nome válido.")