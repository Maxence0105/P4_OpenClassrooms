from tinydb import TinyDB
from models.model import Player


class Display():
	def display_menu(self, options):
		for option in options:
			print(option, options[option])

	def display_player(self):
		print('ID, NOM, PRENOM, AGE, SEXE, POINT\n\n')
		player = Player()
		players = player.db.all()
		element = db.get(self.player)
		id = element.doc_id
		for player in players:
			print(id , player[name], player[firstname], player[age], player[sex], player[elo], '\n')

	def display_separator(self):
		print('==========================\n')

	def display_tournament(self, tournaments):
		print('NOM, DATE, LIEU\n')
		tournament = Tournament()
		tournaments = tournament.db.all()
		element = db.get(self.tournament)
		id = element.doc_id
		for tournament in tournaments:
			print(id, tournament[name], tournament[date], tournament[place])

	def display_message(self, message):
		print(message)
		
	def display_round(self, round):
		for match in round:
			print(player_one, '\n', player_two, '\n\n')


	
#key=player.elo, reverse=True