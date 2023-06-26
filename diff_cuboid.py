# ********************
# CUBOIDES Y VOL�MENES
# ********************


def run(cuboid1: list, cuboid2: list) -> float:
    # TU C�DIGO AQU�

    rmult1 = 1
    rmult2 = 1
    for i in cuboid1:
            rmult1 = rmult1 * i
    for i in cuboid2:
        rmult2 = rmult2 * i


    vol_diff = rmult1 - rmult2 
    if vol_diff < 0:
        vol_diff *= -1

    return vol_diff


if __name__ == '__main__':
    run([2, 2, 3], [5, 4, 1])