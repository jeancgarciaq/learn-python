# ************************
# D�GITOS EN ORDEN INVERSO
# ************************


def run(number: int) -> list:
    # TU C�DIGO AQU�
    cadena = str(number)
    invertido = cadena[::-1]
    enteros = []
    for i in invertido:
        enteros.append(int(i))

    rev_digits = enteros

    return rev_digits


if __name__ == '__main__':
    run(35231)