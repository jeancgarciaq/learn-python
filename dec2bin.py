# *****************
# DECIMAL A BINARIO
# *****************


def run(num: int) -> str:
    # TU C�DIGO AQU�
    prefijo = bin(num)
    cadena = prefijo.partition('b')
    to_bin = cadena[2]

    return to_bin


if __name__ == '__main__':
    run(11)