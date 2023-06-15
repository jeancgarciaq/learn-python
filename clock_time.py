# *********************
# CONTANDO MILISEGUNDOS
# *********************


def run(hours: int, minutes: int, seconds: int) -> float:
    # TU C�DIGO AQU�
    hora = 3600000
    minutos = 60000
    segundos = 1000
    calculo = (hours * hora)+(minutes * minutos)+(seconds * segundos)

    time_since_midnight = calculo

    return time_since_midnight


if __name__ == '__main__':
    run(0, 1, 1)