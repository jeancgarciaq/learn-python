# *************************
# D�GITO DE CONTROL DEL NIF
# *************************


def run(nif: str) -> str:
    # TU C�DIGO AQU�
    if(nif.isnumeric()):
        caracteres = str(nif)
        if(caracteres.startswith('7')):
            wnif = caracteres + 'J' 
        elif(caracteres.startswith('6')):
            wnif = caracteres + 'F'
        elif(caracteres.startswith('4')):
            wnif = caracteres + 'T'
    
    return wnif


if __name__ == '__main__':
    run('78654355')