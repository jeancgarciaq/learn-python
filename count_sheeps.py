# ***************
# CONTANDO OVEJAS
# ***************


def run(num_sheeps: int) -> str:
    # TU C�DIGO AQU�
    if(num_sheeps == 0):
        sleep = ''
    elif(num_sheeps >= 1):
        oveja = 'sheep...'
        sleep = oveja * num_sheeps

    return sleep


if __name__ == '__main__':
    run(0)