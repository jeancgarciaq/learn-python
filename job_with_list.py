#Creamos la lista
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune"]

#Solicitamos al usuario el nombre de un plante del sistema solar
user_planet = input("Please enter the name of the planet (with a capital letter to start)")

#Buscamos el planeta en la lista
planet_index = planets.index(user_planet)

#Desplegamos el o los planetas cercanos al sol similares a los que escogió el usuario
print("Here are the planets closer than " + user_planet)
print(planets[0:planet_index])

#Desplegamos los planetas más lejos del sol
print("Here are the planets further than " + user_planet)
print(planets[planet_index + 1:])