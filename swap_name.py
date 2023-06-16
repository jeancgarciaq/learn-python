# ****************
# NOMBRE VICEVERSA
# ****************


def run(fullname: str) -> str:
    # TU C�DIGO AQU�
    separar = fullname.split(' ', maxsplit=1)
    swapname = separar[1] + ' ' + separar[0]

    return swapname


if __name__ == '__main__':
    run('John McClane')