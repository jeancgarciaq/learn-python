# *********************
# ELIMINANDO DUPLICADOS
# *********************


def run(nums_dups: list) -> list:
    # TU C�DIGO AQU�
    nums_unique = []
    #Usando un bucle for, cumple la solicitud
    #for numero in nums_dups:
        #if numero not in nums_unique:
            #nums_unique.append(numero)

    #Por lista de comprension, cumple la solicitud
    #[nums_unique.append(numero) for numero in nums_dups if numero not in nums_unique]

    #Utilizando los métodos count y remove, funciona pero no mantiene el orden original
    #for numero in nums_dups:
        #while(nums_dups.count(numero) > 1):
            #nums_dups.remove(numero)
            #nums_unique = nums_dups
    
    #Convirtiendo a conjunto, también lo hace pero ordena de mayor a menor
    #nums_unique = list(set(nums_dups))

    #Convirtiendo a un diccionario, cumple la solicitud
    nums_unique = list(dict.fromkeys(nums_dups))

    return nums_unique


if __name__ == '__main__':
    run([2, 3, 2, 2, 1, 5, 4, 2, 4, 9])