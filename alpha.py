text = 'hola-MUNDO'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    if not char in ALPHABET:
        print('Se han encontrado caracteres no alfabéticos')
        break
else:
    print('Todos los caracteres son alfabéticos')
