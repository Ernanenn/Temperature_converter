def converter_temperatura():
    """Converte uma temperatura para todas as escalas (Fahrenheit, Celsius, Kelvin)."""

    while True:
        temperatura_inicial = input("Digite a temperatura e a unidade (F, C ou K) ou 'sair' para encerrar: ").upper()
        if temperatura_inicial == 'SAIR':
            break

        try:
            valor = float(temperatura_inicial[:-1])
            unidade = temperatura_inicial[-1]

            if unidade not in ['F', 'C', 'K']:
                print("Unidade inválida. Use F para Fahrenheit, C para Celsius ou K para Kelvin.")
                continue

            if valor < 0:
                print("A temperatura deve ser um valor positivo.")
                continue

            # Realiza as conversões necessárias
            if unidade == 'F':
                celsius = (5/9) * (valor - 32)
                kelvin = celsius + 273.15
            elif unidade == 'C':
                fahrenheit = (valor * 9/5) + 32
                kelvin = valor + 273.15
            else:  # unidade == 'K'
                fahrenheit = (valor - 273.15) * 9/5 + 32
                celsius = valor - 273.15

            # Exibe os resultados em todas as escalas, exceto a de entrada
            print(f"{valor}{unidade} equivale a:")
            if unidade != 'F':
                print(f"| Fahrenheit: {fahrenheit:.2f}°F |")
            if unidade != 'C':
                print(f"| Celsius:    {celsius:.2f}°C  |")
            if unidade != 'K':
                print(f"| Kelvin:     {kelvin:.2f}°K  |")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número seguido da unidade (F, C ou K).")

if __name__ == "__main__":
    converter_temperatura()