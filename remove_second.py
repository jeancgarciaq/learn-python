# *************************
# NO ME INTERESAN LOS PARES
# *************************
#Elminar de 2 en 2 elementos a partir del segundo índice de una lista

def run(items: list) -> list:
    # TU C�DIGO AQU�
    filter = items[::2]

    return filter


if __name__ == '__main__':
    run([1, 2, 1, 2, 1, 2])