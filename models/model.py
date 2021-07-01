from tinydb import TinyDB, Query

class Player():
	def __init__(self, id = None, name = None, firstname = None, age = None, sex = None, elo = None):
		self.name = name
		self.firstname = firstname
		self.age = age
		self.sex = sex
		self.elo = elo
		self.db = TinyDB('db.json')
		self.id = id
		self.players_table = db.table('players')

	def save_player(self):
		db = TinyDB('db.json')
		players_table = db.table('players')
		self.players_table.insert({'name' : self.name, 'firstname': self.firstname, 'age': self.age, 'sexe': self.sex, 'elo': self.elo})


	def switch_elo(self, value):
		players = Query()
		self.db.update({'elo': value}, players.id == self.id)



class Tournament():
	def __init__(self, id = None, name = None, start_date = None, place = None, description = None, rounds = 4, time_control = None, end_date = None, players = None):
		self.rounds = rounds
		self.time_control = time_control 
		self.name = name
		self.start_date = star_date
		self.end_date = end_date
		self.place = place
		self.description = description
		self.db = TinyDB('db.json')
		self.id = id
		self.players = players

	def save_tournament(self):
		tournaments_table = db.table('tournaments')
		self.tournaments_table.insert({'nom' : self.name, 'date': self.date, 'lieu': self.place, 'description': self.description})

class Match:
    def __init__(self, player_one, player_two, score_player_one, score_player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.score_player_one = score_player_one
        self.score_player_two = score_player_two
        self.matches = (
            [player_one, score_player_one],
            [player_two, score_player_two],
        )

    def result_matches(self):
    	score_player_one =+
    	
class Round:
	def __init__(self):
		self.name = name
		self.start_date = star_date
		self.end_date = end_date
		self.player_chosen = player_chosen

	def first_versus(self, player):
		display_player.sorted(key=player.elo, reverse=True)[player_chosen]
		for i in range 4:
			player_one = player_chosen[i-1] 
			player_two = player_chosen[i+3]

	def versus_player(self, player):
		display_player.sorted(key=score_player, reverse=True)[player_chosen]
		for i in range 4:
			player_one = player_chosen[i-1]
			player_two = player_chosen[i]
		

'''
		player = Player(name= self.name,firstname= self.firstname,age= self.age, sex= self.sex, elo= self.elo)

	
	def serialize_player(self):
		return {
    	'name': self.name,
    	'firstname' : self.firstname,
    	'age': self.age,
    	'sexe': self.sex,
    	'elo': self.elo
}

	def serialize_tournament(self):
	    return {
	    'current_round': self.current_round,
	    'name': self.name,
	    'place': self.place,
	    'start_date': self.start_date,
	    'end_date': self.end_date,
	    'rounds': self.serialize_rounds,
	    'players': self.serialize_players,
	    'time_control': self.time_control,
	    'description': self.description,
	        }

	def serialize_rounds(self):
        round_serialized = []
        for round in self.rounds:
            round_serialized.append(round.serialize)
        return round_serialized
'''