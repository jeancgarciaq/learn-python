# *************
# SUMA REPETIDA
# *************


def run(n: int) -> int:
    # TU C�DIGO AQU�
    if(n == 0):
        result = 0
    elif(n <= 9):
        numero = str(n)
        numero1 = numero * 2
        numero2 = numero * 3
        entero = int(numero1)
        entero1 = int(numero2)
        result = n + entero + entero1
    elif(n >= 10):
        print("Introduzca un número entre 0 y 9")
    
    return result

if __name__ == '__main__':
    run(3)