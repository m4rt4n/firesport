#!/usr/bin/env python3.6

###############################################################################
#
#	Author: Martin Bačo
#	Name: FiresportAttack
#	verze: 0.1
#
#	Description:
#		Simulátor hasičské sportovní disciplíny "Požární útok"
# simulátor k výpočtu časů v požárním útoku. Součástí je i modul
# FSgenerator.py, který dodá potřebné objekty pro inicializaci FireAttacku 
#
###############################################################################

class FireAttack:
	"""simulace požárního útoku, první musí být inicializována třída Weather
	a vložena jako argument: instance=FireAttack(weather)"""
	
	def __init__(self, lenght=80, weather=False, team=False):
		self._lenght = lenght
		#self._engine = engine
		self._team = team
		self._weather = weather
		#self._track = track
		self.__log = list()
	
	# def __str__(self):
	# 	return str("Team: {0}\nWeather: {1}\nTrack: {2}\nEngine: {3}\nLenght: {4}\n".format(self._team, self._weather, self._track, self._engine, self._lenght))
	
	def _set_log(self, message):
		self.__log.append(message)
	
	def get_log(self, lines=0):
		if lines:
			return self.__log[len(self.__log)-1]
		else:
			return self.__log

	def start(self):
		if (self._lenght and self._weather and self._team and self._track):
			pass
		else:
			pass
#########################################################################
	
	
from FSgenerator import *
gen = FSgenerator()
jmena = gen.get_names()
atributy = gen.get_atributes(jmena)
pozice = gen.get_positions(jmena)
masina = gen.get_engine()
pocasi = gen.get_weather()
trat = gen.get_track()
sdh_brumov = gen.get_team("Brumov", trat, masina, atributy, pozice)
delka = 80

attack = FireAttack(delka, pocasi, sdh_brumov)
#testprint
print("---------------------------\n")
print("print(pocasi):>{0}\n".format(pocasi))
print("print(attack):> ..\n{0}\n".format(attack))
print("<<konec kodu>>")



		