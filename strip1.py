# *************************
# QUITANDO PRIMERO Y �LTIMO
# *************************


def run(text: str) -> str:
    # TU C�DIGO AQU�
    inicio = text[0]
    fin = text[-1]
    stext = text.lstrip(inicio).rstrip(fin)

    return stext


if __name__ == '__main__':
    run('What can I do')