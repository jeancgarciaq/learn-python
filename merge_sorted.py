# ***************
# MEZCLA ORDENADA
# ***************


def run(values1: list, values2: list) -> list:
    # TU C�DIGO AQU�
    unidos = [values1, values2]
    juntos = []

    for i in unidos:
        juntos += i
    
    for position in range(len(juntos) - 1):
        minimum = position
        for i in range(position+1, len(juntos)):
            if juntos[i] < juntos[minimum]:
                minimum = i
        juntos[position], juntos[minimum] = juntos[minimum], juntos[position]
    
    diccionario = list(dict.fromkeys(juntos))
    
    merged = diccionario

    return merged


if __name__ == '__main__':
    run([1, 2, 3, 4], [1, 1, 2, 3, 4, 5])