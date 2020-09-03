'''
IDEAS TO ADD:
Small:
	Undo option
Big:
	AI player
	GUI

'''

import cards
from cards import Color
from player import Player

import random, math


class Board():

	def __init__(self, num_players):
		num_victory_cards = 4 + math.ceil(float(num_players) / 2) * 4
		self.num_estates = num_victory_cards
		self.num_dutchies = num_victory_cards
		self.num_provinces = num_victory_cards
		self.num_curses = (num_players - 1) * 10
		self.num_copper = 60 - 7 * num_players
		self.num_silver = 40
		self.num_gold = 30
		self.action_cards = []
		self.num_action_cards = [10 for x in range(10)]

		# Get 10 random action cards for the board and sort them by price
		action_list = random.sample(range(0, len(cards.action)), 10)
		for x in action_list:
			self.action_cards.append(cards.action[list(cards.action)[x]])
		self.action_cards.sort(reverse=True, key=lambda e : e['cost'])

	def available_cards(self):
		"""
		Returns set of available cards

		:returns:   set of available cards
		:rtype:     Set: {'estate', 'dutchy', 'province', ...}
		"""
		available = set()
		if self.num_estates > 0:
			available.add('estate')
		if self.num_dutchies > 0:
			available.add('dutchy')
		if self.num_provinces > 0:
			available.add('province')
		if self.num_curses > 0:
			available.add('curse')
		if self.num_copper > 0:
			available.add('copper')
		if self.num_silver > 0:
			available.add('silver')
		if self.num_gold > 0:
			available.add('gold')
		for i in range(len(self.action_cards))
			if self.num_action_cards[i] < 0:
				available.add(self.action_cards[i]['name'])
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
			print("{:^5}| {:^13} | {:^5}".format(card['cost'], card['name'], self.num_action_cards[i]))
			i += 1
		print()

		# Treasure Cards
		print(Color.BOLD + Color.YELLOW + 'Treasure Cards:' + Color.END)
		print(Color.BOLD + Color.BLUE + "Cost |  Card  | Value | Left" + Color.END)
		print("{:^5}| {:^6} | {:^5} | {:^5}".format(6, 'Gold', 3, self.num_gold))
		print("{:^5}| {:^6} | {:^5} | {:^5}".format(3, 'Silver', 2, self.num_silver))
		print("{:^5}| {:^6} | {:^5} | {:^5}".format(1, 'Copper', 0, self.num_copper))
		print()


		# Victory Cards
		print(Color.BOLD + Color.GREEN + 'Victory Cards:' + Color.END)
		print(Color.BOLD + Color.BLUE + "Cost |     Card      | VP | Left" + Color.END)
		print("{:^5}| {:^13} | {:>2} | {:^5}".format(6, 'Province', 6, self.num_provinces))
		print("{:^5}| {:^13} | {:>2} | {:^5}".format(6, 'Dutchy', 3, self.num_dutchies))
		print("{:^5}| {:^13} | {:>2} | {:^5}".format(6, 'Estate', 1, self.num_estates))
		print("{:^5}| {:^13} | {:^2} | {:^5}".format(6, 'Curse', -1, self.num_curses))
		print()



def main():

	# Set up game
	num_players = 2 #int(input("Number of players: "))
	if num_players < 2:
		print("Not enough players")
		return
	elif num_players > 4:
		print("Too many players")
		return
	players = [Player() for x in range(0, num_players)]
	#print(players[0].hand)

	board = Board(num_players)

	# Main game loop
	game_done = False
	play_order = random.sample([x for x in range(1,num_players+1)], num_players)
	i_play_order = 0
	while not game_done:
		board.display()
		print(Color.RED + "Player {}'s turn".format(play_order[i_play_order]) + Color.END)
		current_player = players[play_order[i_play_order]-1]
		current_player.display_hand()

		# Action phase
		while 1:
			choice = None
			while choice is None:
				try:
					choice = int(input('Choose an option:\n1. Show board\n2. Read action card description\n3. Use action ({} actions left)\n4. End action phase\n>> ' \
						.format(current_player.num_actions)))
					if not 0 < choice < 5:
						choice = None
						raise ValueError()
				except ValueError:
					print("ERROR: Please input a number between 1 and 5: ")

			if choice == 1:
				board.display()
			elif choice == 2:
				card_to_read = input("Name of action card: ").lower()
				cards.print_action_details(card_to_read)
			elif choice == 3:
				pass
			elif choice == 4:
				print()
				break
			print()

		# Buy phase
		while 1:
			choice = int(input('Choose an option:\n1. Show board\n2. Read action card description\n3. Buy card ({} buys left)\n4. End turn\n>> ' \
				.format(current_player.num_buys)))
			while not 0 < choice < 5:
				choice = input("Please input a number: ")

			if choice == 1:
				board.display()
			elif choice == 2:
				card_to_read = input("Name of action card: ").lower()
				cards.print_action_details(card_to_read)
			elif choice == 3:
				if current_player.num_buys > 0:
					# Calculate total money in hand
					total_money = 0
					treasure_in_hand = []

					# Compile list of treasures in hand
					for card_key in current_player.hand:
						if cards.get_type(card_key) == 'treasure':
							total_money += cards.treasure[card_key]['value']
							treasure_in_hand.append(cards.treasure[card_key])

					# Buy card
					print("Total treasure: " + Color.YELLOW + "${}".format(total_money) + Color.END)
					to_buy = input("Card to buy: ").lower()
					print(board.action_cards)
					# If card is available
					if to_buy in board.available_cards:
						# Check if player has enough treasure to purchase
						if cards.dictionary[to_buy]['cost'] > total_money:
							print(Color.RED + "Not enough treasure!" + Color.END)
							print()
							continue

						# Select the treasures to use to purchase
						needed_treasure = cards.dictionary[to_buy]['cost']
						to_remove = []
						while needed_treasure > 0:
							print("Select the treasure you wish to use:")
							for i in range(len(treasure_in_hand)):
								print("{}: ".format(i+1) + Color.YELLOW + "{} ${}".format(treasure_in_hand[i]['name'], \
								 treasure_in_hand[i]['value']) + Color.END)

							to_spend = None
							while to_spend is None:
								try:
									to_spend = int(input(">> "))
									if 0 > to_spend > len(treasure_in_hand):
										to_spend = None
										raise ValueError
								except ValueError:
									print("Enter a valid choice")

							needed_treasure -= treasure_in_hand[to_spend-1]['value']
							to_remove.append(treasure_in_hand.pop(to_spend-1)['name'].lower())

						confirm = input("Confirm purchase?(y,n): ")
						if confirm == 'y':
							for card in to_remove:
								current_player.buy(to_remove, to_buy)

					else:
						print("Card not found")
				else:
					print("No buys left!")
			elif choice == 4:
				print()
				break
			print()

		# Clean up
		current_player.reset()
		i_play_order += 1

		#game_done = True

if __name__ == "__main__":
    main()
