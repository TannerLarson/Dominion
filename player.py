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

	def shuffle():
		pass

	def draw(num = 1):
		if len(draw_pile) < num:
			temp = draw_pile[:num]
			shuffle_deck()
			draw_pile.insert(0, temp)
		self.hand = self.draw_pile[:num]
		self.draw_pile = self.draw_pile[num:]

	def buy(self):
		pass

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