# ****************
# CONTEO REGRESIVO
# ****************


def run(n: int) -> list:
    # TU C�DIGO AQU�
    ordenar = []
    if n >= 1:
        for i in range(1, n + 1):
            ordenar.append(i)
            invertido = sorted(ordenar, reverse=True)
        rev_nums = invertido
    elif n == 0:
        rev_nums = []
    
    return rev_nums


if __name__ == '__main__':
    run(0)