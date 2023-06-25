# ************

# VALOR M�NIMO

# ************
def run(values: list) -> int:

    # TU C�DIGO AQU�

    min_value = values[0]

    for i in values:
        if i < min_value:
            min_value = i

    return min_value



if __name__ == '__main__':
    run([-11, 10, -6, 15, -1])