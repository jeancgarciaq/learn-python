# ******************
# DISTANCIA EUCL�DEA
# ******************
import math

def run(x1: float, y1: float, x2: float, y2: float) -> float:
    # TU C�DIGO AQU�
    distance = math.sqrt(((x2 - x1)**2)+((y2 - y1)**2))

    return distance


if __name__ == '__main__':
    run(3, 5, -7, -4)
    run(2.1, 4.3, -2.3, 8.5)
    run(0.1, 0.2, -0.1, -0.2)