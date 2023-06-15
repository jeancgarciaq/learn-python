# ********************************
# OBTENIENDO EL N�MERO DE PALABRAS
# ********************************


def run(text: str) -> int:
    # TU C�DIGO AQU�
    dividir = text.split()
    num_words = len(dividir)

    return num_words


if __name__ == '__main__':
    run('Before software can be reusable it first has to be usable')