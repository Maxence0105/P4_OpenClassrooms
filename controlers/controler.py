from views.view import Display
from models.model import Player
from models.model import Tournament

class Menu:
	def __init__(self):
		self.view = Display()

		self.menu_principal = {
	'1' : 'Gestion des joueurs',
	'2' : 'Gestion des tournois',
	'3' : 'Rapport',
	'Q' : 'Quitter'
}

		self.menu_tournois = {
	'1' : 'Creer un tournois',
	'2' : 'Selectionner un tournois en cours',
	'Q' : 'Quitter'
}

		self.menu_joueur = {
	'1' : 'Ajouter un joueur',
	'2' : 'Afficher/Modifier les joueurs',
	'Q' : 'Quitter'
}


	def home(self):
		self.view.display_separator()
		self.view.display_menu(self.menu_principal)
		response = input('Votre choix?\n')
		if not response in self.menu_principal:
			print('Erreur, ce choix n\'éxiste pas.')
			self.home()
		elif response =='Q':
			exit()
		elif response =='1':
		# = Gestion des joueurs
			self.players()
		elif response =='2':
			self.tournaments()

	def tournaments(self):
		self.view.display_separator()	
		self.view.display_menu(self.menu_tournois)
		response = input('Votre choix?\n')
		if not response in self.menu_tournois:
			self.view.display_message('Erreur, ce choix n\'éxiste pas.')
			self.tournaments
		elif response =='1':
			self.add_tournaments()
			self.view.display_player()
			self.select_player()
		elif response =='2':
			self.view.display_tournament()
			self.select_tournament()
			if first_versus == True
				self.view.display_round()
				for i in range(4)
					self.switch_score()
					self.versus_player()
		elif response =='Q':
			self.home()


	def players(self):
		self.view.display_separator()
		self.view.display_menu(self.menu_joueur)
		response = input('Votre choix?\n')
		if not response in self.menu_joueur:
			self.view.display_message('Erreur, ce choix n\'éxiste pas.')
			self.players()
		elif response =='1':
			self.add_player()
		elif response =='2':
			self.view.display_player()
			self.switch_elo()
			self.players()
		elif response =='Q':
			self.home()

	def add_tournaments(self):
		self.view.display_separator()
		name = input('Nom du Tournois :\n')
		date = input('Entrer la date sous le format JJ-MM-AAAA :\n')
		place = input('Veuillez inscrire le lieu du tournois :\n')
		description = input('Description du tournois: \n')
		tournament = Tournament(None, self.name, self.start_date, self.place, self.description, self.rounds, self.time_control, self.end_date, self.players)
		tournament.save_tournament()
		select_player()
		self.tournaments()

	def add_player(self):
		self.view.display_separator()
		firstname = input('Quel est le Prenom?\n')
		name = input('Quel est le Nom ?\n')
		age = self.input_positiv('Quel est votre age?\n')
		sex = self.input_sex('Quel est votre sexe? (M/F)\n')
		elo = self.input_positiv('Quel est votre classement (elo) ?\n')
		player = Player(None, name, firstname, age, sex, elo)
		player.save_player()
		self.players()


	def input_positiv(self, message):
		while True:
			val = input(message)
			try:
				if int(val) > 0:	
					return val
				self.view.display_message('La valeur doit être au dessus de 0')
			except ValueError:
				self.view.display_message('La valeur doit être un chiffre entier')
			

	def input_sex(self, message):
		while True:
			gender = input(message)
			try:
				if gender == 'F' or 'M':
					return gender
			except ValueError:
				self.view.display_message('Veuillez entrer M pour masculin ou F pour féminin')	
			

	def switch_elo(self):
		id = self.input_positiv('Quel est l\'identifiant du joueur a modifier?\n')
		value = self.input_positiv('Veuillez ecrire le nouvel elo du joueur\n')	
		player = Player()
		player.switch_elo(id, value)

	def switch_score(self):
		response1 = self.float(input('Combien de points à gagner',player_one'?\n')
		score_player_one =+ response1
		response2 = self.float(input('Combien de points à gagner',player_two'?\n')
		score_player_two =+ response2
		return(score_player_one, score_player_two)


	def select_player(self):	
		self.view.display_message('Selectionner les identifiants des 8 joueurs qui participent au tournoi\n')
		for index, player in enumerate(players):
			self.view.display_message(str(index + 1) + ':', player[name])
			response = input('Quel joueur?')
		players_chosen = players[int(response) - 1]
		return(players_chosen)

	def select_tournament(self):
		self.view.display_message('Selectionner le tournoi en cours\n')
		for index, tournament in enumerate(tournaments):
			self.view.display_message(str(index + 1) + ':', tournament[name], tournament[date], tournament[place])
			response = input('Quel tournois?')
		tournament_chosen = tournaments[int(reponse) -1]
		return(tournament_chosen)



		