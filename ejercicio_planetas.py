planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
 }

#Cuantas lunas hay
moons = planet_moons.values();
#Cuantos planetas hay
total_planets = len(planet_moons.keys())

#contador inicia en 0
total_moons = 0
#bucle for
for moon in moons:
    total_moons = total_moons + moon

#promedio
average = total_moons / total_planets

#imprimimos el promedio
print(f'Each planet has an average of {average} moons')