# *****************
# FICHO CUANDO TOCA
# *****************


def run(time: str, offset: int) -> str:
    # TU C�DIGO AQU�
    dividir = time.partition(':')
    hora = int(dividir[0])
    minuto = int(dividir[2])

    if offset % 60 == 0:
        sumar = offset//60 + hora
        final_time = f'{sumar}:{minuto}'
    else:
        horas = offset//60
        minutos = offset%60
        sumarHora = horas + hora
        sumarMinutos = minutos + minuto

        if sumarHora > 24:
            sumarHora -= 24
        
        if sumarMinutos > 59:
            sumarMinutos -= 60
            sumarHora += 1
        
        final_time = f'{sumarHora}:{sumarMinutos}'


    return final_time


if __name__ == '__main__':
    run('17:15', 240)