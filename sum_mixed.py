# ****************
# SUMA HETEROG�NEA
# ****************


def run(items: list) -> int:
    # TU C�DIGO AQU�
    lista1 = []

    for i in items:
        lista1.append(int(i))
            
    sum_items = sum(lista1)

    return sum_items


if __name__ == '__main__':
    run([1, '2', 3, '4', 5])