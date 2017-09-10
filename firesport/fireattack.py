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
	"""simulace požárního útoku"""
	
	def __init__(self, lenght=80, engine=1.5, team=dict(), weather=str(), track=dict()):
		self._lenght = lenght
		self._engine = engine
		self._team = team
		self._weather = weather
		self._track = track

	def __str__(self):
		return str("požární útok na {0} m.".format(self._lenght))

	
	def set_engine(self, engine):
		self._engine = engine

	def set_weather(self, weather):
		self._weather = weather
	
	def set_team(self, team=dict()):
		self._team = team

	def set_track(self, track=dict()):
		self._track = track
	
	def status(self):
		print("Team: {0}\nWeather: {1}\nTrack: {2}\nEngine: {3}\nLenght: {4}\n".format(self._team, self._weather, self._track, self._engine, self._lenght))

	def start(self):
		pass

attack80=FireAttack()
attack100=FireAttack(100)
print(attack80)
print(attack100)
attack80.status()
quit()
		