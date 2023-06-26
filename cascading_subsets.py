# ***********************
# SUBCONJUNTOS EN CASCADA
# ***********************


def run(values: list, size: int) -> list:
    # TU C�DIGO AQU�
    cascading = [values[i:i + size] for i in range(0, len(values)) if len(values[i:i+size]) == size]
    
    return cascading


if __name__ == '__main__':
    run([1, 2, 3, 4], 3)