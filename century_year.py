# **************************
# BUSCANDO EL SIGLO ADECUADO
# **************************


def run(year: int) -> int:
    # TU C�DIGO AQU�
    siglo = (year - year % 100) // 100

    if(year%100 != 0):
        aumento = 1
    else:
        aumento = 0
    
    century = siglo + aumento
    
    return century


if __name__ == '__main__':
    run(1705)
    run(1900)
    run(1601)
    run(2000)
    run(1999)