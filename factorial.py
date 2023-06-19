# ************************************
# CALCULANDO EL FACTORIAL DE UN N�MERO
# ************************************


def factorial(n):
    # TU C�DIGO AQU�
    if n == 0:
        return 1
    elif n < 0:
        return None
    else:
        numero = 1
        for i in range(1, n + 1):
            numero *= i 
    return numero

factorial(5)