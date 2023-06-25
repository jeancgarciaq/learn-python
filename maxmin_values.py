# *********************
# VALOR M�XIMO Y M�NIMO
# *********************


def run(values: list) -> tuple:
    # TU C�DIGO AQU� 
    max_value = min_value = values[0]
    for i in values:
        if i < min_value:
            min_value = i
        if i > max_value:
            max_value = i

    return max_value, min_value


if __name__ == '__main__':
    run([4, 6, 2, 1, 9, 63, -134, 566])