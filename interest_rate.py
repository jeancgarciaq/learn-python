# *****************
# INTER�S COMPUESTO
# *****************


def run(amount: float, rate: float, years: int) -> float:
    # TU C�DIGO AQU�
    future_amount = amount * (1 + (rate/100)) ** years

    return future_amount


if __name__ == '__main__':
    run(10000, 3.5, 7)
    run(7500, 0.25, 21)
    run(125000, 0.0045, 9)