# *************
# N ELEVADO A N
# *************


def run(values: list, power: int) -> int:
    # TU C�DIGO AQU�
    longitud = len(values)
    
    if power > longitud - 1:
        result = -1
    else:
        numero = values[power]
        result = numero ** power

    return result


if __name__ == '__main__':
    run([1, 2, 3, 4], 2)