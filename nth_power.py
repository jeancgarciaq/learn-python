# *************
# N ELEVADO A N
# *************
#

def run(values: list, power: int) -> int:
    # TU C�DIGO AQU�
    #Dada una lista de números enteros positivos y un número no negativo N, calcule el valor del elemento en la posición N elevado a N.
    longitud = len(values)
    

    if power <= longitud - 1:
        result = values[power] ** power
    else:
        result = -1
    

    return result


if __name__ == '__main__':
    run([10, 20, 30, 40, 50], 4)
    