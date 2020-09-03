import random, math, cards
from cards import Color


class Board():

	def __init__(self, num_players):
		"""
		Constructs a new board

		:param      num_players:  The number of players (Currently can only be 2-4)
		:type       num_players:  int
		"""
		num_victory_cards = 4 + math.ceil(float(num_players) / 2) * 4
		self.num_cards = {
			'estate': num_victory_cards,
			'dutchy': num_victory_cards,
			'province': num_victory_cards,
			'curse': (num_players - 1) * 10,
			'copper': 60 - 7 * num_players,
			'silver': 40,
			'gold': 30,
			'action': [10 for x in range(10)]
		}
		self.action_cards = []
		self.num_empty_piles = 0

		# Get 10 random action cards for the board and sort them by price
		action_list = random.sample(range(0, len(cards.action)), 10)
		for x in action_list:
			self.action_cards.append(cards.action[list(cards.action)[x]])
		self.action_cards.sort(reverse=True, key=lambda e : e['cost'])

	def take_card(self, to_take):
		"""
		Takes a card off the board

		:param      to_take:  Card to be removed
		:type       to_take:  String

		"""
		if to_take in self.num_cards:
			# We don't have an action card
			if self.num_cards[to_take] < 1:
				print("No card to take!")
				return

			self.num_cards[to_take] -= 1
			if self.num_cards[to_take] <= 0:
				self.num_empty_piles += 1


	def available_cards(self):
		"""
		Returns set of available cards

		:returns:   set of available cards
		:rtype:     Set: {'estate', 'dutchy', 'province', ...}
		"""
		available = set()
		if self.num_cards['estate'] > 0:
			available.add('estate')
		if self.num_cards['dutchy'] > 0:
			available.add('dutchy')
		if self.num_cards['province'] > 0:
			available.add('province')
		if self.num_cards['curse'] > 0:
			available.add('curse')
		if self.num_cards['copper'] > 0:
			available.add('copper')
		if self.num_cards['silver'] > 0:
			available.add('silver')
		if self.num_cards['gold'] > 0:
			available.add('gold')
		for i in range(len(self.num_cards['action'])):
			if self.num_cards['action'][i] > 0:
				available.add(self.action_cards[i]['name'].lower())
		return(available)

	def display(self):
		"""
		Displays the board
		"""
		# Action Cards
		print(Color.BOLD + Color.CYAN + 'Action Cards:' + Color.END)
		print(Color.BOLD + Color.BLUE + "Cost |     Card      | Left" + Color.END)
		i = 0
		for card in self.action_cards:
			print("{:^5}| {:^13} | {:^5}".format(card['cost'], card['name'], self.num_cards['action'][i]))
			i += 1
		print()

		# Treasure Cards
		print(Color.BOLD + Color.YELLOW + 'Treasure Cards:' + Color.END)
		print(Color.BOLD + Color.BLUE + "Cost |  Card  | Value | Left" + Color.END)
		print("{:^5}| {:^6} | {:^5} | {:^5}".format(6, 'Gold', 3, self.num_cards['gold']))
		print("{:^5}| {:^6} | {:^5} | {:^5}".format(3, 'Silver', 2, self.num_cards['silver']))
		print("{:^5}| {:^6} | {:^5} | {:^5}".format(1, 'Copper', 0, self.num_cards['copper']))
		print()


		# Victory Cards
		print(Color.BOLD + Color.GREEN + 'Victory Cards:' + Color.END)
		print(Color.BOLD + Color.BLUE + "Cost |     Card      | VP | Left" + Color.END)
		print("{:^5}| {:^13} | {:>2} | {:^5}".format(6, 'Province', 6, self.num_cards['province']))
		print("{:^5}| {:^13} | {:>2} | {:^5}".format(6, 'Dutchy', 3, self.num_cards['dutchy']))
		print("{:^5}| {:^13} | {:>2} | {:^5}".format(6, 'Estate', 1, self.num_cards['estate']))
		print("{:^5}| {:^13} | {:^2} | {:^5}".format(6, 'Curse', -1, self.num_cards['curse']))
		print()