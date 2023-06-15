# **********************
# ANIMALES SUPER R�PIDOS
# **********************


def run(speed_km_h: float) -> float:
    # TU C�DIGO AQU�
    km = 100000
    segundo = 3600
    calculo = (speed_km_h * km)/segundo
    speed_cm_s = int(calculo)

    return speed_cm_s


if __name__ == '__main__':
    run(1.08)