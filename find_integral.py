# *********************

# ENCUENTRA LA INTEGRAL

# *********************



def run(symbol: str) -> str:

    # TU C�DIGO AQU�

    separar = symbol.partition(',')

    base = int(separar[0])
    division = base // (int(separar[2]) + 1)

    integral = f'{division}x^{int(separar[2]) + 1}'

    return integral


if __name__ == '__main__':

    run('3,2')