# *******************
# NO ERES CONSECUTIVO
# *******************


def run(values: list) -> int:
    # TU C�DIGO AQU�

    if len(values) == 0 or len(values) == 1:
        target = None
    else:
        for i in range(len(values) - 1):
            if values[i] == values[i + 1] - 1:
                target = None
            else:
                target = values[i + 1]
                break
                
    return target


if __name__ == '__main__':
    run([1, 2, 3, 4, 6, 7, 8])