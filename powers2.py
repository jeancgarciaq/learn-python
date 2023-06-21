# **************
# POTENCIAS DE 2
# **************


def run(num_powers: int) -> list:
    # TU C�DIGO AQU�
    powers2 = []

    if num_powers == 0:
        powers2.append(2**num_powers)
    else:
        for i in range(num_powers + 1):
            powers2.append(2**i) 

    return powers2

if __name__ == '__main__':
    run(0)