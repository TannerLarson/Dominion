class Card():

	def __init__(self, data):
		self.name = data['name']
		self.cost = data['cost']
		self.description = data['description']
		if 'execute' in data:
			self.execute = data['execute']
		if 'draw' in data:
			self.draw = data['draw']
		if 'action' in data:
			self.action = data['action']
		if 'buy' in data:
			self.buy = data['buy']

def print_action_details(card_name):
	"""
	Prints details of an action card

	:param      card_name:  The card name
	:type       card_name:  String
	"""
	if card_name in dictionary and dictionary[card_name]['type'] == 'action':
		print('\033[96m') # Make the card cyan
		print("Name: {}".format(action[card_name]['name']))
		print("Cost: {}".format(action[card_name]['cost']))
		print("Description: {}".format(action[card_name]['description']))

		# End coloring
		print('\033[0m')
	else:
		print("Action card not found!")
	print()

def get_type(card_key):
	if card_key in dictionary:
		return dictionary[card_key]['type']
	else:
		print("Card not found")
		return None


######################################
# Add color and bold/underline to text
######################################
class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


####################################################################
# CARD DICTIONARIES
# - Each name must be unique, including across different card types
####################################################################

treasure = {
	
	'copper': {
		'name': "Copper",
		'cost': 0,
		'value': 1
	},

	'silver': {
		'name': "Silver",
		'cost': 3,
		'value': 2
	},

	'gold': {
		'name': "Gold",
		'cost': 6,
		'value': 3
	},
}

victory = {
	
	'estate': {
		'name': "Estate",
		'cost': 2,
		'points': 1
	},

	'dutchy': {
		'name': "Dutchy",
		'cost': 5,
		'points': 3
	},

	'province': {
		'name': "Province",
		'cost': 8,
		'points': 6
	},

	'curse': {
		'name': "Curse",
		'cost': 0,
		'points': -1
	}
}


####################################################################
# Base
####################################################################

# ACTION FUNCTIONS

def artisan(player, other_players, board):
	"""
	Gain a card to your hand costing up to 5 treasure. Put a card from your
	hand onto your deck
	"""
	pass
	
def bandit(player, other_players, board):
	"""
	Gain a Gold Each other player reveals the top 2 cards of their deck,
	trashes a revealed Treasure other than Copper, and discards the rest
	"""
	pass
	
def bureaucrat(player, other_players, board):
	"""
	Gain a silver onto your deck. Each other player reveals a Victory card
		 from their hand and puts it onto their deck (or reveals a hand with 
		 no Victory cards)
	"""
	pass
	
def cellar(player, other_players, board):
	"""
	Action: 1
	Discard any number of cards, then draw that many
	"""
	pass
	
def chapel(player, other_players, board):
	"""
	Trash up to 4 cards from your hand
	"""
	for i in range(4):
		player.display_hand()
		choice = None
		while choice is None:
			try:
				choice = int(input("Select number of card you want to trash (0 to quit): "))
				if not 0 <= choice < len(player.hand):
					choice = None
					raise ValueError()
			except ValueError:
				print("ERROR: Please input a number between 0 and {}: ".format(len(player.hand)))
		if choice == 0:
			return
		player.hand.pop(choice-1)

	
def council_room(player, other_players, board):
	"""
	Draw 4
	Buy + 1
	Each other player draws a card
	"""
	pass

def festival(player, other_players, board):
	"""
	Buy + 1
	Action + 2
	+ $2
	"""
	pass

def harbinger(player, other_players, board):
	"""
	"Look through your discard pile. You may put a card from it onto your deck
	Draw 1
	Action + 1
	"""
	pass

def laboratory(player, other_players, board):
	"""
	Draw 2
	Action + 1
	"""
	player.draw(2)
	player.num_actions += 1

def library(player, other_players, board):
	"""
	Draw until you have 7 cards in hand, skipping any Action cards
		 you choose to; set those aside, discarding them
	"""
	pass

def market(player, other_players, board):
	"""
	Draw 1
	Actions + 1
	Buy + 1
	+ $1
	"""
	pass

def merchant(player, other_players, board):
	"""
	The first time you play a Silver this turn + 1 treasure
	Draw 1
	Actions + 1
	"""
	pass

def militia(player, other_players, board):
	"""
	Each other player discards down to 3 cards
	+ $2
	"""
	pass

def mine(player, other_players, board):
	"""
	You may trash a Treasure from your hand.  Gain
		a Treasure to your hand costing up to 3 treasure more than
	"""
	pass

def moat(player, other_players, board):
	"""
	When another player plays an Attack card, you 
		may first reveal this from your hand, to be unaffected by it
	Draw 2
	"""
	pass

def moneylender(player, other_players, board):
	"""
	You may trash a Copper from your hand for +3
	"""
	pass

def poacher(player, other_players, board):
	"""
	Discard a card per empty Supply pile
	Draw 1
	Action + 1
	+ $1
	"""
	pass

def remodel(player, other_players, board):
	"""
	Trash a card from your hand. Gain a card costing up to 2 Treasure more than it.
	"""
	pass

def sentry(player, other_players, board):
	"""
	Look at the top 2 cards of your deck.  Trash and/or discard any number of them.  Put the rest back on top in any order
	"""
	pass

def smithy(player, other_players, board):
	"""
	Draw 3
	"""
	pass

def throne_room(player, other_players, board):
	"""
	You may play an Action card from your hand twice
	"""
	pass

def vassal(player, other_players, board):
	"""
	Discard the top card of your deck.  If it's an Action card, you may play it
	+ $2
	"""
	pass

def village(player, other_players, board):
	"""
	Draw 1
	Actions + 2
	"""
	pass

def witch(player, other_players, board):
	"""
	Each other player gains a Curse
	Draw 2
	"""
	pass

def workshop(player, other_players, board):
	"""
	Gain a card costing up to 4 Treasure
	"""
	pass

# Action dictionary

action = {

	'artisan': {
		'name': "Artisan",
		'cost': 6,
		'description': "Gain a card to your hand costing up to 5"
			" treasure.\nPut a card from your hand onto your deck.",
		'execute': artisan
	},

	'bandit': {
		'name': "Bandit",
		'cost': 5,
		'description': "Gain a Gold\n\
			Each other player reveals the top 2 cards of their deck, "
			"trashes a revealed Treasure other than Copper, and discards"
			"the rest.",
		'execute': bandit
	},

	'bureaucrat': {
		'name': "Bureaucrat",
		'cost': 4,
		'description': "Gain a silver onto your deck.\nEach other "
			"player reveals a Victory card from their hand and puts it onto "
			"their deck (or reveals a hand with no Victory cards).",
		'execute': bureaucrat
	},

	'cellar': {
		'name': "Cellar",
		'cost': 2,
		'description': "Discard any number of cards, then draw that many.",
		'execute': cellar
	},

	'chapel': {
		'name': "Chapel",
		'cost': 2,
		'description': "Trash up to 4 cards from your hand.",
		'execute': chapel
	},

	'council_room': {
		'name': "Council Room",
		'cost': 5,
		'description': "Each other player draws a card.",
		'execute': council_room
	},

	'festival': {
		'name': "Festival",
		'cost': 5,
		'description': "",
		'execute': festival
	},

	'harbinger': {
		'name': "Harbinger",
		'cost': 3,
		'description': "Look through your discard pile.\nYou may put a "
		"card from it onto your deck.",
		'execute': harbinger
	},

	'laboratory': {
		'name': "Laboratory",
		'cost': 5,
		'description': "",
		'execute': laboratory
	},

	'library': {
		'name': "Library",
		'cost': 5,
		'description': "Draw until you have 7 cards in hand, skipping any"
		"Action cards you choose to; set those aside, discarding them "
		"afterwards",
		'execute': library
	},

	'market': {
		'name': "Market",
		'cost': 5,
		'description': "",
		'execute': market
	},

	'merchant': {
		'name': "Merchant",
		'cost': 3,
		'description': "The first time you play a Silver this turn, "
		"+1 Treasure",
		'execute': merchant
	},

	'militia': {
		'name': "Militia",
		'cost': 4,
		'description': "Each other player discards down to 3 cards "
		"in hand.",
		'execute': militia
	},

	'mine': {
		'name': "Mine",
		'cost': 5,
		'description': "You may trash a Treasure from your hand.  Gain"
		" a Treasure to your hand costing up to 3 treasure more than"
		" it.",
		'execute': mine
	},

	'moat': {
		'name': "Moat",
		'cost': 2,
		'description': "When another player plays an Attack card, you "
		"may first reveal this from your hand, to be unaffected by it.",
		'execute': moat
	},

	'moneylender': {
		'name': "Moneylender",
		'cost': 4,
		'description': "You may trash a Copper from your hand for +3"
		" Treasure.",
		'execute': moneylender
	},

	'poacher': {
		'name': "Poacher",
		'cost': 4,
		'description': "Discard a card per empty Supply pile.",
		'execute': poacher
	},

	'remodel': {
		'name': "Remodel",
		'cost': 4,
		'description': "Trash a card from your hand. Gain a card "
		"costing up to 2 Treasure more than it.",
		'execute': remodel
	},

	'sentry': {
		'name': "Sentry",
		'cost': 5,
		'description': "Look at the top 2 cards of your deck.  Trash "
		"and/or discard any number of them.  Put the rest back on top"
		" in any order.",
		'execute': sentry
	},

	'smithy': {
		'name': "Smithy",
		'cost': 4,
		'description': "",
		'execute': smithy
	},

	'throne_room': {
		'name': "Throne Room",
		'cost': 4,
		'description': "You may play an Action card from your hand twice.",
		'execute': throne_room
	},

	'vassal': {
		'name': "Vassal",
		'cost': 3,
		'description': "Discard the top card of your deck.  If it's an "
		"Action card, you may play it.",
		'execute': vassal
	},

	'village': {
		'name': "Village",
		'cost': 3,
		'description': "",
		'execute': village
	},

	'witch': {
		'name': "Witch",
		'cost': 5,
		'description': "Each other player gains a Curse",
		'execute': witch
	},

	'workshop': {
		'name': "Workshop",
		'cost': 3,
		'description': "Gain a card costing up to 4 Treasure",
		'execute': workshop
	}
}




#################################################################
# Big dicitionary with every card in it
#################################################################


dictionary = {

	'artisan': {
		'type': 'action',
		'name': "Artisan",
		'cost': 6,
		'description': "Gain a card to your hand costing up to 5"
			" treasure.\nPut a card from your hand onto your deck.",
		'execute': ''
	},

	'bandit': {
		'type': 'action',
		'name': "Bandit",
		'cost': 5,
		'description': "Gain a Gold\n\
			Each other player reveals the top 2 cards of their deck, "
			"trashes a revealed Treasure other than Copper, and discards"
			"the rest.",
		'execute': ''
	},

	'bureaucrat': {
		'type': 'action',
		'name': "Bureaucrat",
		'cost': 4,
		'description': "Gain a silver onto your deck.\nEach other "
			"player reveals a Victory card from their hand and puts it onto "
			"their deck (or reveals a hand with no Victory cards).",
		'execute': ''
	},

	'cellar': {
		'type': 'action',
		'name': "Cellar",
		'cost': 2,
		'description': "Discard any number of cards, then draw that many.",
		'execute': '',
		'action': 1
	},

	'chapel': {
		'type': 'action',
		'name': "Chapel",
		'cost': 2,
		'description': "Trash up to 4 cards from your hand.",
		'execute': ''
	},

	'council_room': {
		'type': 'action',
		'name': "Council Room",
		'cost': 5,
		'description': "Each other player draws a card.",
		'execute': '',
		'draw': 4,
		'buy': 1
	},

	'festival': {
		'type': 'action',
		'name': "Festival",
		'cost': 5,
		'description': "",
		'action': 2,
		'buy': 1,
		'value': 2
	},

	'harbinger': {
		'type': 'action',
		'name': "Harbinger",
		'cost': 3,
		'description': "Look through your discard pile.\nYou may put a "
		"card from it onto your deck.",
		'execute': '',
		'draw': 1,
		'action': 1
	},

	'laboratory': {
		'type': 'action',
		'name': "Laboratory",
		'cost': 5,
		'description': "",
		'execute': '',
		'draw': 2,
		'action': 1
	},

	'library': {
		'type': 'action',
		'name': "Library",
		'cost': 5,
		'description': "Draw until you have 7 cards in hand, skipping any"
		"Action cards you choose to; set those aside, discarding them"
		"afterwards",
		'execute': ''
	},

	'market': {
		'type': 'action',
		'name': "Market",
		'cost': 5,
		'description': "",
		'execute': '',
		'draw': 1,
		'action': 1,
		'buy': 1,
		'value': 1
	},

	'merchant': {
		'type': 'action',
		'name': "Merchant",
		'cost': 3,
		'description': "The first time you play a Silver this turn, "
		"+1 Treasure",
		'execute': '',
		'draw': 1,
		'action': 1
	},

	'militia': {
		'type': 'action',
		'name': "Militia",
		'cost': 4,
		'description': "Each other player discards down to 3 cards "
		"in hand.",
		'execute': '',
		'value': 2
	},

	'mine': {
		'type': 'action',
		'name': "Mine",
		'cost': 5,
		'description': "You may trash a Treasure from your hand.  Gain"
		" a Treasure to your hand costing up to 3 treasure more than"
		" it.",
		'execute': ''
	},

	'moat': {
		'type': 'action',
		'name': "Moat",
		'cost': 2,
		'description': "When another player plays an Attack card, you "
		"may first reveal this from your hand, to be unaffected by it.",
		'execute': '',
		'draw': 2
	},

	'moneylender': {
		'type': 'action',
		'name': "Moneylender",
		'cost': 4,
		'description': "You may trash a Copper from your hand for +3"
		" Treasure.",
		'execute': ''
	},

	'poacher': {
		'type': 'action',
		'name': "Poacher",
		'cost': 4,
		'description': "Discard a card per empty Supply pile.",
		'execute': '',
		'draw': 1,
		'action': 1,
		'value': 1
	},

	'remodel': {
		'type': 'action',
		'name': "Remodel",
		'cost': 4,
		'description': "Trash a card from your hand. Gain a card "
		"costing up to 2 Treasure more than it.",
		'execute': ''
	},

	'sentry': {
		'type': 'action',
		'name': "Sentry",
		'cost': 5,
		'description': "Look at the top 2 cards of your deck.  Trash "
		"and/or discard any number of them.  Put the rest back on top"
		" in any order.",
		'execute': ''
	},

	'smithy': {
		'type': 'action',
		'name': "Smithy",
		'cost': 4,
		'description': "",
		'execute': '',
		'draw': 3
	},

	'throne_room': {
		'type': 'action',
		'name': "Throne Room",
		'cost': 4,
		'description': "You may play an Action card from your hand twice.",
		'execute': ''
	},

	'vassal': {
		'type': 'action',
		'name': "Vassal",
		'cost': 3,
		'description': "Discard the top card of your deck.  If it's an "
		"Action card, you may play it.",
		'execute': '',
		'value': 2
	},

	'village': {
		'type': 'action',
		'name': "Village",
		'cost': 3,
		'description': "",
		'execute': '',
		'draw': 1,
		'action': 2
	},

	'witch': {
		'type': 'action',
		'name': "Witch",
		'cost': 5,
		'description': "Each other player gains a Curse",
		'execute': '',
		'draw': 2
	},

	'workshop': {
		'type': 'action',
		'name': "Workshop",
		'cost': 3,
		'description': "Gain a card costing up to 4 Treasure",
		'execute': ''
	},

	#### Treasure ##########################################
	
	'copper': {
		'type': 'treasure',
		'name': "Copper",
		'cost': 0,
		'value': 1
	},

	'silver': {
		'type': 'treasure',
		'name': "Silver",
		'cost': 3,
		'value': 2
	},

	'gold': {
		'type': 'treasure',
		'name': "Gold",
		'cost': 6,
		'value': 3
	},

	#### Victory #############################################3
	
	'estate': {
		'type': 'victory',
		'name': "Estate",
		'cost': 2,
		'points': 1
	},

	'dutchy': {
		'type': 'victory',
		'name': "Dutchy",
		'cost': 5,
		'points': 3
	},

	'province': {
		'type': 'victory',
		'name': "Province",
		'cost': 8,
		'points': 6
	},

	'curse': {
		'type': 'victory',
		'name': "Curse",
		'cost': 0,
		'points': -1
	}
}