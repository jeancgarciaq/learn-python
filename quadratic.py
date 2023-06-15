# *************************
# ECUACI�N DE SEGUNDO GRADO
# *************************
import math

def run(a: int, b: int, c: int) -> tuple:
    # TU C�DIGO AQU�
    AC = 4 * a * c
    B2 = b ** 2
    A2 = 2 * a
    B = -(b)
    
    x1 = (B + math.sqrt(B2 - AC))/A2
    x2 = (B - math.sqrt(B2 - AC))/A2

    return x1, x2


if __name__ == '__main__':
    run(4, -6, 2)
    run(1, 2, -3)
    run(-1, -2, 8)