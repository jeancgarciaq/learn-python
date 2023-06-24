# **************
# SUMA INVERTIDA
# **************


def run(numbers: list) -> int:
    # TU C�DIGO AQU�
    sumar = 0
    for x in numbers:
        sumar += x * -1
    add_inv = sumar

    return add_inv


if __name__ == '__main__':
    run([1, 2, 3, 4, 5])