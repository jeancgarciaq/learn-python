# OPCIÓN A
while True:
    name = input('¿Su nombre? ')
    if name.istitle():
        break
    print('Error. Debe escribirlo correctamente, Formato Título')

# OPCIÓN B
while not (name := input('¿Su nombre? ').istitle()):
    print('Error. Debe escribirlo correctamente, Formato Título')
