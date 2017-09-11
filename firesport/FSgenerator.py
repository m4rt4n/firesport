#!/usr/bin/env python3
class FSgenerator:
	"""
	Třída služící ke generování náhodných seznamů a slovníků pro obsluhu
	třídy FireAttack.
	"""
	ENGINES = (
		0.8, 1.2, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1
		)
	NAMES = { #key0 = jména, key1 = příjmení
		0 : ["Jan", "Petr", "Pavel", "Tomáš", "Lukáš", "Rudolf", "Lubomír", "Filip","Jaroslav", "Václav", "Radek"],
		1 : ["Bačo", "Novák", "Zemánek", "Koubský", "Leixner", "Suchý", "Rozehnal", "Urban", "Lysák", "Lysáček"]
		}
	POSITIONS = (
		#u pozic se pořadí nemění, nikdy! vždy a všude bude platit toto pořadí
		#jde se podle pozic od košaře směrem dopředu
		"košař", "nalévač", "strojník", "béčkař", "rozdělovač", "LP", "PP"
		)
	WEATHER = [
		#pozice druhu počasí určuje zároveň jeho náročnost
		["slunečné", "jasné", "polojasné", "zamračené", "deštivé", "mrazivé"],
		["bezvětrné", "s mírným vítrem", "se silným vítrem", "s extrémním vítrem"]
		]
	import random as _random
	def __init__(self):
		pass

	def get_names(self, count=7):
		"""vrací list() jmen, defaultně 7"""
		prepared_names = list()
		for _ in range(0, count):
			prepared_names.append("{0} {1}".format(self.NAMES[0][self._random.randint(0,len(self.NAMES[0])-1)],self.NAMES[1][self._random.randint(0,len(self.NAMES[1])-1)]))
		return prepared_names #seznam 7 jmen

	def get_engine(self):
		"""vrací sílu mašinu typu float"""
		return float(self.ENGINES[self._random.randint(0,len(self.ENGINES)-1)])

	def get_weather(self):
		"""vrací str(), kodovane počasí. pozicePočasí-poziceVítr, např 2polojasné-0bezvětrné"""
		weather0 = self._random.randint(0,len(self.WEATHER[0])-1)
		weather1 = self._random.randint(0,len(self.WEATHER[1])-1)
		return str("{0}{1}-{2}{3}".format(weather0,self.WEATHER[0][weather0],weather1, self.WEATHER[1][weather1]))

	def get_positions(self, names=False):
		"""přiřazuje jména k pozicím, defaultně vytvoří i jména. Přijímá
		get_names() jako nepodmínečný argument. Vrací seznam typu ["kosar":"jmeno příjmení"]"""
		if not names:
			names = self.get_names()
		positions=list()
		for x in range(0, 7):
			positions.append("{0}:{1}".format(self.POSITIONS[x],names[x]))
		return positions

	def get_atributes(self, names=False, minimal=50):
		"""Přiřazuje atributy k jménům, vrací množinu jméno:atributy. Nepovinný
		argument je get_names() a int() který udává minimální hranici v rozsahu
		1-100, defaultně nastaveno 50.
			vrací seznam stringu v podobě:
		jméno:kvalita:potencial:rychlost:sila:dovednost
		"""
		
		if not names:
			names = self.get_names()
		atributes = list()
		for x in range(0, 7):
			atributes.append("{0}:{1}:{2}:{3}:{4}:{5}".format(names[x], self._random.randint(minimal, 101), self._random.randint(minimal, 101), self._random.randint(minimal, 101), self._random.randint(minimal, 101), self._random.randint(minimal, 101)))
		return atributes
	
	def get_track(self):
		"""generace trati"""
		return "a"
	
	def get_team(self, name, track=False, engine=False, atributes=False, positions=False):
		"""Skládaá tým ze jmána, mašiny, atributů, pozic. Vrací team v podobě seznamu. Pokud mu nejsou vloženy atributy nebo pozice, tak si krom mašiny generuje vše saám. objekt jméno musí být vloženo při inicializaci"""

		if not engine:
			engine = self.get_engine()
		elif not track:
			track = self.get_track()
		elif not (atributes or positions):
			names = self.get_names()
			atributes = self.get_atributes(names)
			positions = self.get_positions(names)
		team = []
		return team
###################################################################
# gen = FSgenerator()
# print(gen.get_engine())
# names = gen.get_names()
# print(names)
# print(gen.get_weather())
# print(gen.get_positions())
# print(gen.get_atributes(names))
# print(gen.get_track())
		
