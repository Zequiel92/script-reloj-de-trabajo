'''
	En este segundo ejercicios tendréis que crear un script que nos diga si 
	es la hora de ir a casa. Tendréis que hacer uso del modulo time. 
	Necesitaréis la fecha del sistema y poder comprobar la hora.

	En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, 
	haréis una operación para calcular el tiempo que queda de trabajo.

'''

import datetime

import time


inicio_hora = '07'
inicio_minuto = '00'

final_hora = '14'
final_minuto = '00'

# Obtener la hora y fecha del usuario
hour_pc = datetime.datetime.now()

# si la hora y minutos del usuario es igual o sobrepasa la hora acordada al terminar el trabajo
if hour_pc.strftime('%H') >= final_hora:

	if hour_pc.strftime('%M') >= final_minuto:
		print(f'Son las {hour_pc.hour}:{hour_pc.minute}, es hora de irse a casa')

elif hour_pc.strftime('%H') == inicio_hora:
	print(f'Son las {hour_pc.hour}:{hour_pc.minute}')

	# calcular cuantas horas de trabajo quedan
	horas_restantes = int(hour_pc.hour) - int(final_hora)
	minutos_restantes = int(hour_pc.minute) - int(final_minuto)

	print(f'Quedan {horas_restantes} horas y {minutos_restantes} minutos para irse a casa') 