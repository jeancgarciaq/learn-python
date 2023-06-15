# ***************
# PRECIO SIN IGIC
# ***************


def run(price_with_igic: float, igic: float) -> float:
    # TU C�DIGO AQU�
    normalizado = igic/100
    parametrizado = 1 + normalizado
    calculo = price_with_igic/parametrizado
    clean_price = round(calculo, 2)

    return clean_price


if __name__ == '__main__':
    run(120, 7)