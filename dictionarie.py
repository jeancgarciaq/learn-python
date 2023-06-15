#Creacion de un diccionario
planet = {
    'name': 'Earth',
    'moons': 1
}

#Asi imprimimos el nombre
print(planet.get('name'))

# Displays Earth

#Tenemos ésta segunda opción

# planet['name'] is identical to using planet.get('name')
print(planet['name'])

# Displays Earth

#Ejemplo cuando los corchetes invocan un nombre que no existe
#wibble = planet.get('wibble') # Returns None
#wibble = planet['wibble'] # Throws KeyError

#Actualización de valores en un diccionario
planet.update({'name': 'Makemake'})

# name is now set to Makemake

#Otra forma de hacer el llamado para cambiar los valores
# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Using square brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79


#Se puede añadir claves, conforme se amerite
planet['orbital period'] = 4333

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }

#Se puede eliminar una clave con su valor.
planet.pop('orbital period')

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }

#Los diccionarios pueden almacenar otros diccionarios:
# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }

#Para recuperar los valores guardados
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')

# Output: Jupiter polar diameter: 133709
