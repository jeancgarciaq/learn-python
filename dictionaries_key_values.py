#diccionario

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

#acceder a los valores por las claves
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

# Output:
# october: 3.5cm
# november: 4.2cm
# december: 2.1cm

#acceder a los valores sin las claves
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

# Because december exists, the value will be 3.1
