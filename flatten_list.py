# ***************
# APLANA LA LISTA
# ***************


def run(elements: list) -> list:
    # TU C�DIGO AQU�
    #usando bucle for
    lista1 = []
    lista2 = []
    flatten_elements = []

    for element in elements:
        if isinstance(element, int):
            lista1.append(element)
        elif isinstance(element, str):
            lista1.append(element)
        elif isinstance(element, list):
            lista2 += element
              
    flatten_elements = lista1 + lista2

    return sorted(flatten_elements)


if __name__ == '__main__':
    run([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])