# *************************
# LA MULTIPLICACI�N DE JACK
# *************************


def run(n: int) -> int:
    # TU C�DIGO AQU�
    absoluto = abs(n)
    numero = str(absoluto)
    exponente = len(numero)

    result = n * 5**exponente

    return result


if __name__ == '__main__':
    run(3)