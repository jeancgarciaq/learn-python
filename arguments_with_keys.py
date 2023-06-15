from datetime import timedelta, datetime

#Argumento con valor predeterminado
def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

arrival_time(hours=0)

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

arrival_time("Moon")

arrival_time("Orbit", hours=0.13)

#Sin indicar el número de argumentos
def variable_length(*args):
    print(args)

variable_length()

variable_length("one", "two")

variable_length(None)

#Ejemplo con varios argumentos
def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"

sequence_time(4, 14, 18)
sequence_time(4, 14, 48)

#Argumentos sin determinar números de palabras claves
def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day="Wednesday", pilots=3)

#Ejemplo
def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", pilot="Michael Collins")