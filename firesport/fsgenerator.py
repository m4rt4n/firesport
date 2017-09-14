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
		0 : ["Jan", "Petr", "Pavel", "Tomáš", "Lukáš", "Rudolf", "Lubomír", "Filip","Jaroslav", "Václav", "Radek", "Jiří", "Josef"],
		1 : ["Bačo", "Novák", "Zemánek", "Koubský", "Leixner", "Suchý", "Rozehnal", "Urban", "Lysák", "Lysáček", "Mifka", "Buček", "Ovesný", "Strnka", "Bařinka"]
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
	SURFACES = [

		"tráva", "tráva s kobercem", "zámecká dlažba", "beton", "asfalt", "tartan"
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
		jméno:kvalita:potencial:rychlost:sila:dovednost:reakce
		"""
		
		if not names:
			names = self.get_names()
		atributes = list()
		for x in range(0, 7):
			atributes.append("{0}:{1}:{2}:{3}:{4}:{5}:{6}".format(names[x], self._random.randint(minimal, 100), self._random.randint(minimal, 100), self._random.randint(minimal, 100), self._random.randint(minimal, 100), self._random.randint(minimal, 100), self._random.randint(minimal, 100)))
		return atributes
	
	def get_track(self, strain=1, pole=0):
		"""
		prní prarametr typ náběhu, druhý typ zbytku hřiště. Náběh je od startu 
		za káď, v šířce 15m (30 polí). Káď má tozměr 1x1.5m (2x3políčka)

		generace trati, rozměr 17mx105m (34X210 polí), trat je 4Dpole, rozdělené po 0.5m. v prvni vrstvě je určeno o jaký typ povrchu a jeho stupen kvality (O-100) se jedná. V další vrstvě hodnota podmáčenosti(0-100) a v poslední rozmístění nářaadí (základna, káď, značky..)"""
		
		#jeste dedelat random výběr strain a pole, misto defaultu	
		track = []
		for ly in range(3):
			layer = []
			for li in range(36):
				line = []
				for x in range(210):
					if ly == 0: #první vrstva:typ povrchu
						if x <= 30: #šířka náběhu
							line.append(strain)
						else:
							line.append(pole)
					elif ly == 1: #druhá vrstva: podmáčenost(0)
						line.append(0)
					elif ly == 2: #třetí vrstva, rozmístění vercajku
						if (1<=li<=3) and (20<=x<22):# kad
							line.append("LAMFEŠT")
						elif (12<=li<=15) and (18<=x<22):# zakladna
							line.append("ZÁKLADNA")
						else: # nic
							line.append(False)
				layer.append(line)
			track.append(layer)
		return track
	def get_team(self, name, engine=False, atributes=False, positions=False):
		"""Skládaá tým ze jmána, mašiny, atributů, pozic. Vrací team v podobě seznamu. Pokud mu nejsou vloženy atributy nebo pozice, tak si krom mašiny generuje vše saám. objekt jméno musí být vloženo při inicializaci"""
		if not engine:
			engine = self.get_engine()
		if not (atributes or positions):
			names = self.get_names()
			atributes = self.get_atributes(names)
			positions = self.get_positions(names)
		team = {
			"jméno" : str(name),
			"mašina" : float(engine),
			self.POSITIONS[0] : atributes[0].split(":"),
			self.POSITIONS[1] : atributes[1].split(":"),
			self.POSITIONS[2] : atributes[2].split(":"),
			self.POSITIONS[3] : atributes[3].split(":"),
			self.POSITIONS[4] : atributes[4].split(":"),
			self.POSITIONS[5] : atributes[5].split(":"),
			self.POSITIONS[6] : atributes[6].split(":")
			}
		return team
###################################################################
#gen = FSgenerator()
# print(gen.get_engine())
#names = gen.get_names()
# print(names)
# print(gen.get_weather())
# print(gen.get_positions())
#print(gen.get_atributes(names))
#print(gen.get_track(1, 0))
#track = gen.get_track(3, 4)
#print(track)
#print(gen.get_team("brumov"))
