import random, copy, cards
from cards import Color

class Player():

	def __init__(self):
		"""
		Player constructor
		"""
		self.num_actions = 1
		self.num_buys = 1
		self.discard_pile = []

		self.draw_pile = ['copper','copper','copper','copper','copper', 
			'copper','copper','copper','copper','copper'] # Last element in draw_pile list is the top of the deck
		random.shuffle(self.draw_pile)
		self.hand = self.draw_pile[:5]
		self.draw_pile = self.draw_pile[5:]

	def draw(self, num = 1):
		"""
		Draw cards from the draw pile

		:param      num:             Number of cards to draw
		:type       num:             int: 3 / 5
		"""
		print('Draw pile: {}'.format(self.draw_pile))
		for i in range(num):
			assert(len(self.draw_pile) > 0), "Length of deck before draw: {}".format(len(self.draw_pile))
			self.hand.append(self.draw_pile.pop())
			if len(self.draw_pile) <= 0:
				self.refill_deck()


	def refill_deck(self):
		"""
		Shuffle discard pile and make it the deck

		:raises     AssertionError:  Draw pile must be empty
		"""
		print("Reshuffling discard into draw")
		assert len(self.draw_pile) == 0, "Draw pile should be empty"
		self.draw_pile = self.discard_pile
		random.shuffle(self.draw_pile)
		self.discard_pile = []

	def buy(self, to_buy, treasure_used = []):
		"""
		Updates player when buying a card

		:param      treasure_used:  List of treasure used to buy card
		:type       treasure_used:  List: [copper, copper, gold, silver]
		:param      to_buy:         Card being bought
		:type       to_buy:         String: 'moat' / 'province'
		"""
		# Remove cards from hand
		for card in treasure_used:
			self.hand.remove(card)

		# Discard cards
		treasure_used.append(to_buy)
		self.discard(treasure_used)
		self.num_buys -= 1

	def reset_hand(self):
		"""
		Reset data for player when their turn ends
		"""
		self.num_actions = 1
		self.num_buys = 1
		self.discard(self.hand)
		self.hand = []
		self.draw(5)

	def discard(self, to_discard):
		"""
		Send a card to player discard pile

		:param      to_discard:  List or string of card(s) to send to discard pile
		:type       to_discard:  List: [copper, copper, moat] / 'gold'
		"""
		if isinstance(to_discard, list):
			self.discard_pile += to_discard
		elif isinstance(to_discard, str):
			self.discard_pile.append(to_discard)

	def display_hand(self):
		"""
		Displays hand
		"""
		i = 1
		print("Hand:")
		for card in self.hand:
			card_actual = cards.dictionary[card]
			if card_actual['type'] == 'action':
				print(str(i) + '. ' + Color.CYAN + card_actual['name'] + Color.END)
			elif card_actual['type'] == 'treasure':
				print(str(i) + '. ' + Color.YELLOW + card_actual['name'] + " ${}".format(card_actual['value']) + Color.END)
			elif card_actual['type'] == 'victory':
				print(str(i) + '. ' + Color.GREEN + card_actual['name'] + Color.END)
			else:
				print(card_actual['name'])
			i += 1
		print()

def use_action(players, board, i_current_player, card_name):
		temp = [self, ]
		cards.action[card_name]['execute'](self, other_players, board)
		self.discard(card_name)
		self.hand.remove(card_name)