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
# výpočy s pčesností na setiny
##############################################################################

from fsgenerator import *
class FireAttack:
	"""simulace požárního útoku"""
	def __init__(self, lenght=80, track=False, weather=False, team=False):
		print("init start...")
		self._fsgen = FSgenerator()
		self._lenght = lenght
		self._weather = weather
		if not self._weather:self._weather = self._fsgen.get_weather()
		self._team = team
		if not self._team:self._team = self._fsgen.get_team("random")
		self._track = track
		if not self._track:self._track = self._fsgen.get_track()
		self.__log = []
		self._fa_log = []
	
	def __str__(self):
		return str("lenght: {0}\nweather: {1}\nteam:\n{2}\ntrack:\n{3}".format(self._lenght, self._weather, self._team, self._track))
	
	def _set_log(self, message):
		self.__log.append(message)

	def _set_fa_log(self, message):
		self.__log.append(message)
	
	def get_log(self, lines=0):
		"""defaultně vrátí celý log, nepovinný argument je počet posledních řádků z logu"""
		if lines:
			return self.__log[len(self.__log)-1]
		else:
			return self.__log
	
	def show_track(self):
		"""ukáže graficky trat, velikost 17x105"""
		pass

	def x_y_to_x2_y2(self, x_in, y_in, x_end, y_end):
		"""počítání vzáleností polí od sebe navzájem"""
		return int()

	def _fa_preparator(self, man):
		"""počítání tratí 
		vrací:
			{
				"START"	: [[xo,yo],[postihPovrchu]], #
				"1RUN"	: [postih, postih,.],
				"1STOP"	: [[xi,yi],[postihPovrchu]],
				"2RUN"	: [postih,postih,postih..],
				"2DROP"	: [[xi,yi,xo,yo],[postih]], // "2FINAL" : [[xi,yi],[postihPovrchu]]
				"3RUN"	: [postih,postih,..],
				"3FINAL": [[xi,yi],[postihPovrchu]]
			}

		"""
		track={ #začátek společný pro všechny
			"START"	: [[],[]],
			"1RUN"	: [],
			"1STOP"	: [[],[]],
			"2RUN"	: []
			}
		if self._team["košař"][0] == man[0]: #košař
			track["2FINAL"] = []
			track["START"][0].extend([35,15])#startovní pozice
			track["START"][1].extend([self._track[0][track["START"][0][0]][track["START"][0][1]]])
			track["1RUN"].extend([12,15])#pozice zastávky u koše
			#track["1RUN"][1].extend([])#rm
			#temp=[]
			#for x,y in range(12,35+1):
				

		elif self._team["nalévač"][0] == man[0]:#nálévač 
			track["2FINAL"] = []
		elif self._team["strojník"][0] == man[0]:#strojník
			track["2FINAL"] = []
		elif self._team["rozdělovač"][0] == man[0]:#rozdělovač
			track["2FINAL"] = []
		elif self._team["béčkař"][0] == man[0] and self._lenght == 80:#báčkař80
			track["2FINAL"] = []
		else:
			track["2DROP"] = [[],[]]
			track["3RUN"] = []
			track["3FINAL"] = [[],[]]
		

		return track
	def tesst(self):
		print(self._fa_preparator(self._team[self._fsgen.POSITIONS[0]]))
		

	def _fa_start(self, track, time):
		"""pro všechny stejné, pvužit atribut Rychlost, Reakce, kvalita"""
		import random as _random

		return str("_fa_start..end")
	def start(self):
		self._temp_man = []
		#self._temp_
		if not (self._lenght and self._weather and self._team and self._track):
			print("Nemáš vše potřebné...")
		else:
			for x in range(7):
				result_time = 0
				#man= list(jméno:kvalita:potencial:rychlost:sila:dovednost:reakce
				man = self._team[self._fsgen.POSITIONS[x]]
				mantrack = self._fa_preparator(man)
				print(mantrack)
				#první úkon: start >(reakce+?)
				#self._fa_start(mantrack["START"], result_time)
				#první úsek: náběh k místu >(rychlost)
				#druhý úkon: práce na základně >(dovednost)
				#druhý úsek: doběh na místo třetího úkonu >(ryhlost,dovednost,síla), u každé
				#pozice jiný atribut
				#třetí úkon: u koše, nalévače, strojníka, rozdělovače, nebo béčkaře na 80m je finálním
				#třetí úsek: týká se jen proudů po odhození a béčkaře na 100m je doběh na místo
				#čtvrtý úkon: týká se jen proudů, nebo béčkaře na 100m.
#########################################################################
	
print("START MAIN")	
gen = FSgenerator()
jmena = gen.get_names()
atributy = gen.get_atributes(jmena)
pozice = gen.get_positions(jmena)
masina = gen.get_engine()
jmeno = "sdh brumov"
sdh_brumov = gen.get_team(jmeno, masina, atributy, pozice)
#####################################################################
trat = gen.get_track(3,0)
pocasi = gen.get_weather()
delka = 80

attack = FireAttack(delka, trat, pocasi, sdh_brumov)
print("-------------xxx---------")
attack2 = FireAttack(100)
#####################################################################
#testprint
print("---------------------------\n")
print("print(pocasi):>{0}\n".format(pocasi))
#print("print(attack2):> ..\n{0}\n".format(attack2))
#print("print(attack):> ..\n{0}\n".format(attack))
#print("attack2.start():>{0}".format(attack2.start()))
attack2.start()
#attack2.tesst()
print("<<konec kodu>>")
########################################################################
# náhodné poznámky, nápady
# 
# kvalita člana ovlivní jen jeho tréning...


		