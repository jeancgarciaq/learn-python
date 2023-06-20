# *****************************
# SUMA DE LA DIAGONAL PRINCIPAL
# *****************************

#for i in range(len(matrix)):
        #for j in range(len(matrix[i])):
            #print(matrix[i][j])

def run(matrix: list) -> int:
    # TU C�DIGO AQU�
    sum_diagonal = 0

    for i in range(len(matrix)):
        diagonal = matrix[i][i]
        sum_diagonal += diagonal    

    return sum_diagonal


if __name__ == '__main__':
    run([[4, 6, 1], [2, 9, 3], [1, 7, 7]])