person1 = 'piedra'
person2 = 'papel'

if person1 == 'piedra' and person2 == 'papel':
    print(f'Gana {person2}')
elif person1 == 'papel' and person2 == 'piedra':
    print(f'Gana {person1}')
elif person1 == 'papel' and person2 == 'tijera':
    print(f'Gana {person2}')
elif person1 == 'tijera' and person2 == 'papel':
    print(f'Gana {person2}')
elif person1 == 'tijera' and person2 == 'piedra':
    print(f'Gana {person2}')
elif person1 == 'piedra' and person2 == 'tijera':
    print(f'Gana {person1}')