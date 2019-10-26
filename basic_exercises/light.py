"""
Calcular la cantidad de segundos que le toma a la luz viajar del sol a Marte
y mostrar el resultado en pantalla.
"""

seconds_velocity = 300000
minute = 60

mercurio =	57910000 
venus	= 108200000 
tierra =  146600000 
marte	= 227940000 
jupiter	= 778330000 
saturno	= 1429400000 
urano	= 2870990000 
neptuno	= 4504300000 
pluton	= 5934456500 

result_seconds = float(marte) // float(seconds_velocity)
result_minutes = result_seconds // float(minute)

print("mart_light_seconds is:", result_seconds)

print("Time amount of ligth in minutes is:", result_minutes)
