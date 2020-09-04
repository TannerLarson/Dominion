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

action = {

	'artisan': {
		'name': "Artisan",
		'cost': 6,
		'description': "Gain a card to your hand costing up to 5"
			" treasure.\nPut a card from your hand onto your deck.",
		'execute': ''
	},

	'bandit': {
		'name': "Bandit",
		'cost': 5,
		'description': "Gain a Gold\n\
			Each other player reveals the top 2 cards of their deck, "
			"trashes a revealed Treasure other than Copper, and discards"
			"the rest.",
		'execute': ''
	},

	'bureaucrat': {
		'name': "Bureaucrat",
		'cost': 4,
		'description': "Gain a silver onto your deck.\nEach other "
			"player reveals a Victory card from their hand and puts it onto "
			"their deck (or reveals a hand with no Victory cards).",
		'execute': ''
	},

	'cellar': {
		'name': "Cellar",
		'cost': 2,
		'description': "Discard any number of cards, then draw that many.",
		'execute': '',
		'action': 1
	},

	'chapel': {
		'name': "Chapel",
		'cost': 2,
		'description': "Trash up to 4 cards from your hand.",
		'execute': ''
	},

	'council_room': {
		'name': "Council Room",
		'cost': 5,
		'description': "Each other player draws a card.",
		'execute': '',
		'draw': 4,
		'buy': 1
	},

	'festival': {
		'name': "Festival",
		'cost': 5,
		'description': "",
		'action': 2,
		'buy': 1,
		'value': 2
	},

	'harbinger': {
		'name': "Harbinger",
		'cost': 3,
		'description': "Look through your discard pile.\nYou may put a "
		"card from it onto your deck.",
		'execute': '',
		'draw': 1,
		'action': 1
	},

	'laboratory': {
		'name': "Laboratory",
		'cost': 5,
		'description': "",
		'execute': '',
		'draw': 2,
		'action': 1
	},

	'library': {
		'name': "Library",
		'cost': 5,
		'description': "Draw until you have 7 cards in hand, skipping any"
		"Action cards you choose to; set those aside, discarding them "
		"afterwards",
		'execute': ''
	},

	'market': {
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
		'name': "Merchant",
		'cost': 3,
		'description': "The first time you play a Silver this turn, "
		"+1 Treasure",
		'execute': '',
		'draw': 1,
		'action': 1
	},

	'militia': {
		'name': "Militia",
		'cost': 4,
		'description': "Each other player discards down to 3 cards "
		"in hand.",
		'execute': '',
		'value': 2
	},

	'mine': {
		'name': "Mine",
		'cost': 5,
		'description': "You may trash a Treasure from your hand.  Gain"
		" a Treasure to your hand costing up to 3 treasure more than"
		" it.",
		'execute': ''
	},

	'moat': {
		'name': "Moat",
		'cost': 2,
		'description': "When another player plays an Attack card, you "
		"may first reveal this from your hand, to be unaffected by it.",
		'execute': '',
		'draw': 2
	},

	'moneylender': {
		'name': "Moneylender",
		'cost': 4,
		'description': "You may trash a Copper from your hand for +3"
		" Treasure.",
		'execute': ''
	},

	'poacher': {
		'name': "Poacher",
		'cost': 4,
		'description': "Discard a card per empty Supply pile.",
		'execute': '',
		'draw': 1,
		'action': 1,
		'value': 1
	},

	'remodel': {
		'name': "Remodel",
		'cost': 4,
		'description': "Trash a card from your hand. Gain a card "
		"costing up to 2 Treasure more than it.",
		'execute': ''
	},

	'sentry': {
		'name': "Sentry",
		'cost': 5,
		'description': "Look at the top 2 cards of your deck.  Trash "
		"and/or discard any number of them.  Put the rest back on top"
		" in any order.",
		'execute': ''
	},

	'smithy': {
		'name': "Smithy",
		'cost': 4,
		'description': "",
		'execute': '',
		'draw': 3
	},

	'throne_room': {
		'name': "Throne Room",
		'cost': 4,
		'description': "You may play an Action card from your hand twice.",
		'execute': ''
	},

	'vassal': {
		'name': "Vassal",
		'cost': 3,
		'description': "Discard the top card of your deck.  If it's an "
		"Action card, you may play it.",
		'execute': '',
		'value': 2
	},

	'village': {
		'name': "Village",
		'cost': 3,
		'description': "",
		'execute': '',
		'draw': 1,
		'action': 2
	},

	'witch': {
		'name': "Witch",
		'cost': 5,
		'description': "Each other player gains a Curse",
		'execute': '',
		'draw': 2
	},

	'workshop': {
		'name': "Workshop",
		'cost': 3,
		'description': "Gain a card costing up to 4 Treasure",
		'execute': workshop()
	}
}

########################################################################
# ACTION FUNCTIONS
########################################################################

def artisan(player, board):
	"""
	Gain a card to your hand costing up to 5 treasure. Put a card from your
	hand onto your deck
	"""
	pass
	
def bandit(player, board):
	"""
	Gain a Gold Each other player reveals the top 2 cards of their deck,
	trashes a revealed Treasure other than Copper, and discards the rest
	"""
	pass
	
def bureaucrat(player, board):
	"""
	Gain a silver onto your deck. Each other player reveals a Victory card
		 from their hand and puts it onto their deck (or reveals a hand with 
		 no Victory cards)
	"""
	pass
	
def cellar(player, board):
	"""
	Action: 1
	Discard any number of cards, then draw that many
	"""
	pass
	
def chapel(player, board):
	"""
	Trash up to 4 cards from your hand
	"""
	pass
	
def council_room(player, board):
	"""
	Draw 4
	Buy + 1
	Each other player draws a card
	"""
	pass

def festival(player, board):
	"""
	Buy + 1
	Action + 2
	+ $2
	"""
	pass

def harbinger(player, board):
	"""
	"Look through your discard pile. You may put a card from it onto your deck
	Draw 1
	Action + 1
	"""
	pass

def laboratory(player, board):
	"""
	Draw 2
	Action + 1
	"""
	pass

def library(player, board):
	"""
	Draw until you have 7 cards in hand, skipping any Action cards
		 you choose to; set those aside, discarding them
	"""
	pass

def market(player, board):
	"""
	Draw 1
	Actions + 1
	Buy + 1
	+ $1
	"""
	pass

def merchant(player, board):
	"""
	The first time you play a Silver this turn + 1 treasure
	Draw 1
	Actions + 1
	"""
	pass

def militia(player, board):
	"""
	Each other player discards down to 3 cards
	+ $2
	"""
	pass

def mine(player, board):
	"""
	You may trash a Treasure from your hand.  Gain
		a Treasure to your hand costing up to 3 treasure more than
	"""
	pass

def moat(player, board):
	"""
	When another player plays an Attack card, you 
		may first reveal this from your hand, to be unaffected by it
	Draw 2
	"""
	pass

def moneylender(player, board):
	"""
	You may trash a Copper from your hand for +3
	"""
	pass

def poacher(player, board):
	"""
	Discard a card per empty Supply pile
	Draw 1
	Action + 1
	+ $1
	"""
	pass

def remodel(player, board):
	"""
	Trash a card from your hand. Gain a card costing up to 2 Treasure more than it.
	"""
	pass

def sentry(player, board):
	"""
	Look at the top 2 cards of your deck.  Trash and/or discard any number of them.  Put the rest back on top in any order
	"""
	pass

def smithy(player, board):
	"""
	Draw 3
	"""
	pass

def throne_room(player, board):
	"""
	You may play an Action card from your hand twice
	"""
	pass

def vassal(player, board):
	"""
	Discard the top card of your deck.  If it's an Action card, you may play it
	+ $2
	"""
	pass

def vassal(player, board):
	"""
	Draw 1
	Actions + 2
	"""
	pass

def witch(player, board):
	"""
	Each other player gains a Curse
	Draw 2
	"""
	pass

def workshop(player, board):
	"""
	Gain a card costing up to 4 Treasure
	"""
	pass




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