any([True, False, False])
#return True
any([False, False, False])
#return False

str()
#return ''
str(15)
#return '15'

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"

#Error con un argumento vacío
# distance_from_earth()

#Con argumento
distance_from_earth("Moon")
distance_from_earth("Saturn")

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

days_to_complete(238855, 75)

#Funciones como argumentos
total_days = days_to_complete(238855, 75)
round(total_days)

