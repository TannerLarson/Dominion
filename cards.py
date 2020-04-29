class Card():

	def __init__(self, data):
		self.name = data['name']
		self.cost = data['cost']
		self.description = data['description']
		if 'execute' in data:
			self.execute = data['execute']




###################################################################
###################################################################

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
		"Action cards you choose to; set those aside, discarding them"
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
		'execute': ''
	}
}

###################################################################

treasure = {
	
	'c': {
		'name': "Copper",
		'cost': 0,
		'value': 1
	},

	's': {
		'name': "Silver",
		'cost': 3,
		'value': 2
	},

	'g': {
		'name': "Gold",
		'cost': 6,
		'value': 3
	},
}

####################################################################

victory = {
	
	'e': {
		'name': "Estate",
		'cost': 2,
		'points': 1
	},

	'd': {
		'name': "Dutchy",
		'cost': 5,
		'points': 3
	},

	'p': {
		'name': "Province",
		'cost': 8,
		'points': 6
	},

	'c': {
		'name': "Curse",
		'cost': 0,
		'points': -1
	}
}