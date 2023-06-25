# **************
# EL LOBO ACECHA
# **************


def run(farm: list) -> str:
    # TU C�DIGO AQU�
    granja = farm[::-1]
    
    if granja[0] == 'lobo':
        msg = 'No te quiero ver más por aquí, lobo'
    else:
        for x in range(0, len(granja)):
            if granja[x] == 'oveja' and granja[x + 1] == 'lobo':
                numero = x + 1
                msg = f'Cuidado oveja {numero}, el lobo te va a comer'
                break
        
    return msg


if __name__ == '__main__':
    run(['lobo', 'oveja', 'oveja', 'oveja'])