from calculator import calcular


def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite um número válido.")


def main():
    print("Calculadora")
    print("Operações: + - * /")
    print("Digite 'sair' para encerrar.\n")

    while True:
        entrada = input("Primeiro número (ou 'sair'): ")

        if entrada.lower() == "sair":
            print("Programa encerrado.")
            break

        try:
            a = float(entrada)
            operador = input("Operador (+ - * /): ")
            b = ler_numero("Segundo número: ")

            resultado = calcular(a, operador, b)
            print(f"Resultado: {resultado}\n")

        except ValueError as erro:
            print(f"Erro: {erro}\n")


if __name__ == "__main__":
    main()