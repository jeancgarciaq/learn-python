# **********************
# INICIALES DE UN NOMBRE
# **********************


def run(fullname: str) -> str:
    # TU C�DIGO AQU�
    dividir = fullname.split()
    longitud = len(dividir)

    if longitud == 4:
        Primero = ''.join(dividir[0])
        Segundo = ''.join(dividir[1])
        Tercero = ''.join(dividir[2])

        initials = Tercero[0].upper() + '.' + Primero[0].upper() + '.' + Segundo[0].upper() + '.' 
    elif longitud == 3:
        Primero = ''.join(dividir[0])
        Segundo = ''.join(dividir[1])
        Tercero = ''.join(dividir[2])

        initials = Tercero[0].upper() + '.' + Primero[0].upper() + '.' + Segundo[0].upper() + '.' 
    elif longitud == 2:
        Primero = ''.join(dividir[0])
        Segundo = ''.join(dividir[1])

        initials = Segundo[0].upper() + '.' + Primero[0].upper() + '.'  

    return initials


if __name__ == '__main__':
    run('Prado López, Ana Belén')