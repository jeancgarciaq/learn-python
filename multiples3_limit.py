# Escriba un programa que encuentre la mínima secuencia de múltiplos de 3 (distintos) cuya suma sea igual o superior a un valor dado
total_sum = 45
current_sum = 0
current_3mult = 0
print(f'M={current_3mult:2d}: S={current_sum:2d}')

while current_sum < total_sum:
    current_3mult += 3
    current_sum += current_3mult
    print(f'M={current_3mult:2d}: S={current_sum:2d}')
