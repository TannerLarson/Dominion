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

	def alter_hand(to_remove, to_add):
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

		self.hand.append(to_add)

	def reset(self):
		self.num_actions = 1
		self.num_buys = 1
		self.discard_hand
		#self.draw(5)

	def display_hand(self):
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

	def discard_hand(self):
		pass