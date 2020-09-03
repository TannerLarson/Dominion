import random
import cards
from cards import Color

class Player():

	def __init__(self):
		self.discard_pile = []
		
		# Shuffle the draw pile
		self.draw_pile = random.sample(['copper','copper','copper','copper','copper', \
			'copper','copper','estate','estate','estate'], 10)
		self.num_actions = 1
		self.num_buys = 1
		self.hand = self.draw_pile[:5]

		self.draw_pile = self.draw_pile[5:]

	def draw(num = 1):
		if len(draw_pile) < num:
			temp = draw_pile[:num]
			shuffle_deck()
			draw_pile.insert(0, temp)
		self.hand = self.draw_pile[:num]
		self.draw_pile = self.draw_pile[num:]

	def buy(self, to_buy, treasure_used = []):
		"""
		Updates player when buying a card

		:param      treasure_used:  List of treasure used to buy card
		:type       treasure_used:  List: [copper, copper, gold, silver]
		:param      to_buy:         Card being bought
		:type       to_buy:         String: 'moat' / 'province'
		"""
		self.alter_hand(treasure_used)
		self.discard(treasure_used + to_buy)
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
		self.discard_hand
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
		self.discard_pile += to_discard