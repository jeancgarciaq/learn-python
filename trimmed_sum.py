# **************
# SUMA RECORTADA
# **************


def run(values: list) -> int:
    # TU C�DIGO AQU�
    min_value = 1 
    max_value = 1
    longitud = len(values)
    unicos = list(dict.fromkeys(values))

    if longitud <= 2:
        tsum = 0
    else:
        for i in unicos:
            if i > max_value:
                max_value = i
            elif i <= min_value:
                min_value = i

        suma = sum(unicos)

        tsum = suma - max_value - min_value

    return tsum


if __name__ == '__main__':
    #run([6, 2, 1, 8, 10])
    #run([1,1,11,2,3])
    run([])