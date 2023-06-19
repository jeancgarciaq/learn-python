# ************
# VALOR M�XIMO
# ************


def run(values: list) -> int:
    # TU C�DIGO AQU�
    max_value = None

    for numero in values:
        if (max_value is None or numero > max_value):
            max_value = numero

    return max_value


if __name__ == '__main__':
    run([-11, 10, -6, 15, -1])