# ********************
# CALCULANDO M�LTIPLOS
# ********************


def run(x: int, n: int) -> list:
    # TU C�DIGO AQU�
    multiples = []

    for i in range(1, n + 1):
        multiples.append(x*i)

    return multiples


if __name__ == '__main__':
    run(1, 10)