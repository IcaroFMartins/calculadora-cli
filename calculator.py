def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


def calcular(a, operador, b):
    operacoes = {
        "+": somar,
        "-": subtrair,
        "*": multiplicar,
        "/": dividir,
    }

    if operador not in operacoes:
        raise ValueError(f"Operador inválido: {operador}")

    return operacoes[operador](a, b)