# ********************************
# UNA M�TRICA PARA CADENA DE TEXTO
# ********************************


def run(text: str) -> int:
    # TU C�DIGO AQU�
    longitud = len(text)
    a = text.count('a')
    e = text.count('e')
    i = text.count('i')
    o = text.count('o')
    u = text.count('u')

    suma = a + e + i + o + u

    metric = longitud * suma

    return metric


if __name__ == '__main__':
    run('ordenador')