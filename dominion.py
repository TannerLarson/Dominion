'''
IDEAS TO ADD:
Small:
	Undo option
Big:
	AI player
	GUI

'''






import cards
import random 
import math
import copy

######################################
# Add color and bold/underline to text
######################################
class color:
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

	def display(self):
		# Action Cards
		print(color.BOLD + color.CYAN + 'Action Cards:' + color.END)
		print(color.BOLD + color.BLUE + "Cost |     Card      | Left" + color.END)
		i = 0
		for card in self.action_cards:
			print("{:^5}| {:^13} | {:^5}".format(card['cost'], card['name'], self.num_action_cards[i]))
			i += 1
		print()

		# Treasure Cards
		print(color.BOLD + color.YELLOW + 'Treasure Cards:' + color.END)
		print(color.BOLD + color.BLUE + "Cost |  Card  | Value | Left" + color.END)
		print("{:^5}| {:^6} | {:^5} | {:^5}".format(6, 'Gold', 3, self.num_gold))
		print("{:^5}| {:^6} | {:^5} | {:^5}".format(3, 'Silver', 2, self.num_silver))
		print("{:^5}| {:^6} | {:^5} | {:^5}".format(1, 'Copper', 0, self.num_copper))
		print()


		# Victory Cards
		print(color.BOLD + color.GREEN + 'Victory Cards:' + color.END)
		print(color.BOLD + color.BLUE + "Cost |     Card      | VP | Left" + color.END)
		print("{:^5}| {:^13} | {:>2} | {:^5}".format(6, 'Province', 6, self.num_provinces))
		print("{:^5}| {:^13} | {:>2} | {:^5}".format(6, 'Dutchy', 3, self.num_dutchies))
		print("{:^5}| {:^13} | {:>2} | {:^5}".format(6, 'Estate', 1, self.num_estates))
		print("{:^5}| {:^13} | {:^2} | {:^5}".format(6, 'Curse', -1, self.num_curses))
		print()


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
				print(color.CYAN + card_actual['name'] + color.END)
			elif card_actual['type'] == 'treasure':
				print(color.YELLOW + card_actual['name'] + " ${}".format(card_actual['value']) + color.END)
			elif card_actual['type'] == 'victory':
				print(color.GREEN + card_actual['name'] + color.END)
			else:
				print(card_actual['name'])
		print()

	def discard_hand(self):
		pass



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
		print(color.RED + "Player {}'s turn".format(play_order[i_play_order]) + color.END)
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
				break

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
					for card_key in current_player.hand:
						if cards.get_type(card_key) == 'treasure':
							total_money += cards.treasure[card_key]['value']

					to_buy = input("Card to buy: ")
					if to_buy in cards.dictionary:
						pass
					else:
						print("Card not found")
				else:
					print("No buys left!")
			elif choice == 4:
				break

		# Clean up
		current_player.reset()
		i_play_order += 1

		#game_done = True

if __name__ == "__main__":
    main()
