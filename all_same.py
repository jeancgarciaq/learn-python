# *****************************
# SOMOS IGUALES, PERO DISTINTOS
# *****************************


def run(items: list) -> bool:
    # TU C�DIGO AQU�
    longitud = len(items)
    ocurrencia = items.count(items[0])

    if longitud == ocurrencia:
        all_same = True
    else:
        all_same = False

    return all_same


if __name__ == '__main__':
    run([1, 1, 1, 1, 1, 1])