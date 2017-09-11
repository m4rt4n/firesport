#!/usr/bin/env python3.6

###############################################################################
#
#	Author: Martin Bačo
#	Name: FiresportAttack
#	verze: 0.1
#
#	Description:
#		Simulátor hasičské sportovní disciplíny "Požární útok"
#simulátor k výpočtu časů v požárním útoku
#
###############################################################################

class FireAttack:
	"""simulace požárního útoku, první musí být inicializována třída Weather
	a vložena jako argument: instance=FireAttack(weather)"""
	
	def __init__(self, weather, lenght, engine, team=list(), track=dict()):
		self._lenght = lenght
		self._engine = engine
		self._team = team
		self._weather = weather
		self._track = track
		self.__log = tuple()
	
	def __str__(self):
		return str("požární útok na {0} m.".format(self._lenght))
	
	def _set_log(self, message):
		self.__log.append(message)
	
	def get_log(self, lines=0):
		if lines:
			return self.__log[len(self.__log)-1]
		else:
			return self.__log
	
	def set_lenght(self, lenght=int()):
		self._lenght = lenght
	
	def set_engine(self, engine=float()):
		self._engine = engine

	def set_team(self, team=list()):
		self._team = team

	def set_track(self, track=dict()):
		self._track = track
	
	def status(self):
		return "Team: {0}\nWeather: {1}\nTrack: {2}\nEngine: {3}\nLenght: {4}\n".format(self._team, self._weather, self._track, self._engine, self._lenght)

	def start(self):
		pass
#########################################################################
class Team:
	"""Třída reprezentující team, musí být vložen do Fireattack"""
	FENGINES = (0.8, 1.2, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1)
	NAMES = { 
	0 : ["jan", "petr", "pavel", "tomas", "luke", "ruda", "lubos"],
	1 : ["Bačo", "Novák", "Zemánek", "Koubský", "Leixner", "Suchý"]
	}
	POS = ("košař", "nalévač", "strojník", "béčkař", "rozdělovač", "LP", "PP")
	
	def __init__(self, jmeno, engine, atributes, positions):
		#import random as _random
		self.__jmeno = jmeno
		self.__engine = self.__random_engine_generator()
	
	def __str__(self):
		return "tým: {0}\nmašina: {1}\n".format(self.__jmeno, self.__engine)
	
	def __random_engine_generator(self):
		import random as _random
		return self.FENGINES[_random.randint(0,len(self.FENGINES)-1)]
		

	def __random_name_generator(self):
		NAMES = { 
			0 : ["jan", "petr", "pavel", "tomas", "luke", "ruda", "lubos"],
			1 : ["Bačo", "Novák", "Zemánek", "Koubský", "Leixner", "Suchý"]
			}
		import random as _random
		prepared_names = list()
		for _ in range(0,7):
			prepared_names.append("{0} {1}".format(NAMES[0][_random.randint(0,len(NAMES[0])-1)],NAMES[1][_random.randint(0,len(NAMES[1])-1)]))
		return prepared_names #seznam 7 jmen

	def __positions_generator(self, names=list()):
		if not names:
			self.__random_name_generator()
		self.__positions = zip(self.POS,self.__prepared_names)
		return self.__positions
	def status(self):
		pass

	def get_positions(self):
		pass

from FSgenerator import *
gen = FSgenerator()
jmena = gen.get_names()
atributy = gen.get_atributes(jmena)
pozice = gen.get_positions(jmena)
pocasi = gen.get_weather()
masina = gen.get_engine()
delka = 80

attack = FireAttack(pocasi, delka, masina)
#team = Team("Brumov")
#testprint
print("---------------------------\n")
print("print(pocasi):\n{0}\n".format(pocasi))
print("attack.status():\n{0}\n".format(attack.status()))
#print("print(team):\n{0}".format(team))
print("<<konec kodu>>")



		