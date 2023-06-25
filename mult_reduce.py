# ************************
# MULTIPLICACI�N EN CADENA
# ************************


def run(numbers: list) -> int:
    # TU C�DIGO AQU�
    if len(numbers) == 0:
        rmult = 1
    else:
        rmult = 1
        for i in numbers:
            rmult = rmult * i

    return rmult


if __name__ == '__main__':
    run([1, 2, 3, 4])