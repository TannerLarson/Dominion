import random
import cards
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
			'copper','copper','estate','estate','estate'] # Last element in draw_pile list is the top of the deck
		random.shuffle(self.draw_pile)
		self.hand = self.draw_pile[:5]
		self.draw_pile = self.draw_pile[5:]

	def draw(self, num = 1):
		"""
		Draw cards from the draw pile

		:param      num:             Number of cards to draw
		:type       num:             int: 3 / 5

		:raises     AssertionError:  Draw pile must have cards in it
		"""
		for i in range(num):
			assert len(self.draw_pile) > 0, "Can't draw from empty draw pile"
			self.hand.append(self.draw_pile.pop())
			if len(self.draw_pile) <= 0:
				self.discard_to_draw()

	def discard_to_draw(self):
		"""
		Shuffle discard pile and make it the deck

		:raises     AssertionError:  Draw pile must be empty
		"""
		assert len(self.draw_pile) == 0, "Draw pile should be empty"
		self.draw_pile = self.discard_pile
		random.shuffle(self.draw_pile)
		self.discard_pile = []
		print(self.draw_pile)

	def buy(self, to_buy, treasure_used = []):
		"""
		Updates player when buying a card

		:param      treasure_used:  List of treasure used to buy card
		:type       treasure_used:  List: [copper, copper, gold, silver]
		:param      to_buy:         Card being bought
		:type       to_buy:         String: 'moat' / 'province'
		"""
		self.alter_hand(treasure_used)
		self.discard(treasure_used.append(to_buy))
		self.num_buys -= 1

	def alter_hand(self, to_remove = [], to_add = None):
		"""
		Updates player hand with cards to add and remove
		* TODO: Does not check if cards are in hand
		
		:param      to_remove:  List of cards to remove
		:type       to_remove:  List: ['copper', 'silver', 'dutchy']
		:param      to_add:     String of card to add
		:type       to_add:     String: 'moat' / 'gold'
		"""
		for card in to_remove:
			self.hand.remove(card)

		if to_add is not None:
			self.hand.append(to_add)

	def reset(self):
		"""
		Reset data for player when their turn ends
		"""
		self.num_actions = 1
		self.num_buys = 1
		self.discard(self.hand)
		self.hand = []
		self.draw(5)
		#self.draw(5)

	def display_hand(self):
		"""
		Displays hand
		"""
		print("Hand:")
		for card in self.hand:
			card_actual = cards.dictionary[card]
			if card_actual['type'] == 'action':
				print(Color.CYAN + card_actual['name'] + Color.END)
			elif card_actual['type'] == 'treasure':
				print(Color.YELLOW + card_actual['name'] + " ${}".format(card_actual['value']) + Color.END)
			elif card_actual['type'] == 'victory':
				print(Color.GREEN + card_actual['name'] + Color.END)
			else:
				print(card_actual['name'])
		print()

	def discard(self, to_discard):
		"""
		Send a card to player discard pile

		:param      to_discard:  List of cards to send to discard pile
		:type       to_discard:  List: [copper, copper, moat]
		"""
		print("discarding: {}".format(to_discard))
		if to_discard is not None:
			self.discard_pile += to_discard