# **********************
# SUMANDO SOLO POSITIVOS
# **********************


def run(numbers: list) -> int:
    # TU C�DIGO AQU�
    sumar = 0
    for x in numbers:
        if x > 0:
            sumar += x
        
    sum_positive = sumar

    return sum_positive


if __name__ == '__main__':
    run([1, -4, 7, 12])