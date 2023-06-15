# ***
# XOR
# ***


def run(v1: bool, v2: bool) -> bool:
    # TU C�DIGO AQU�
    if(v1 == False and v2 == False):
        xor = False
    elif(v1 == True and v2 == False):
        xor = True
    elif(v1 == False and v2 == True):
        xor = True
    elif(v1 == True and v2 == True):
        xor = False

    return xor

if __name__ == '__main__':
    run(False, False)