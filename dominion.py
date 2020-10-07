'''
IDEAS TO ADD:
Small:
	Undo option
Big:
	AI player
	GUI

'''
from cards import Color
from player import Player
from board import Board

import random, cards, actions


def main():
	"""
	Main game engine
	"""

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
	play_order = [x for x in range(1,num_players+1)]
	random.shuffle(play_order)
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
					choice = int(input('Choose an option:\n1. Show board\n2. Show hand\n3. Read ' + Color.CYAN 
					 	+ 'action' + Color.END + ' card description\n4. Use action ({} actions left)\n5. Undo last move\n6. End action phase\n>> '
						.format(current_player.num_actions)))
					if not 0 < choice <= 6:
						choice = None
						raise ValueError()
				except ValueError:
					print("ERROR: Please input a number between 1 and 6: ")

			if choice == 1:
				board.display()
			elif choice == 2:
				current_player.display_hand()
			elif choice == 3:
				card_to_read = input("Name of action card: ").lower()
				if card_to_read in cards.dictionary:
					if cards.dictionary[card_to_read]['type'] == 'action':
						cards.print_action_details(card_to_read)
					else:
						print("Not an action card!")
				else:
					print("Card not found!")
			elif choice == 4:
				i_action = None
				while i_action is None:
					try:
						i_action = int(input('Please input the number of the action card you want to use (0 to cancel): ')) - 1
						if not -1 <= i_action < len(current_player.hand):
							i_action = None
							raise ValueError()
						if i_action != -1 and cards.dictionary[current_player.hand[i_action]]['type'] != 'action':
							i_action = None
							raise CardTypeError()
					except ValueError:
							print("ERROR: Please input a number between 1 and {}: ".format(len(current_player.hand)))
					except CardTypeError:
						print("Selected card is not an action card!")
				if i_action == -1:
					print()
					continue
				current_player.use_action(current_player.hand[i_action], players, board)
			elif choice == 5:
				print('Undo!')
			elif choice == 6:
				print()
				break
			print()

		# Buy phase
		while 1:
			choice = None
			while choice is None:
				try:
					choice = int(input('Choose an option:\n1. Show board\n2. Show hand\n3. Read ' + Color.CYAN 
					 + 'action' + Color.END + ' card description\n4. Buy card ({} buys left)\n5. Undo last move\n6. End turn\n>> '
						.format(current_player.num_buys)))
					if not 0 < choice <= 6:
						choice = None
						raise ValueError()
				except ValueError:
					print("ERROR: Please input a number between 1 and 6: ")

			if choice == 1:
				board.display()
			elif choice == 2:
				current_player.display_hand()
			elif choice == 3:
				card_to_read = input("Name of action card: ").lower()
				cards.print_action_details(card_to_read)
			elif choice == 4:
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
					# If card is available
					if to_buy in cards.dictionary: #board.available_cards():				PUT THIS LINE BACK IN WHEN DONE TESTING
						# Check if player has enough treasure to purchase
						if cards.dictionary[to_buy]['cost'] > total_money:
							print(Color.RED + "Not enough treasure!" + Color.END)
							print()
							continue

						# Select the treasures to use to purchase
						needed_treasure = cards.dictionary[to_buy]['cost']
						treasure_used = []
						while needed_treasure > 0:
							print("Amount Owed: " + Color.YELLOW + "${}".format(needed_treasure) + Color.END)
							print("Select the treasure you wish to use:")
							for i in range(len(treasure_in_hand)):
								print("{}: ".format(i+1) + Color.YELLOW + "{} ${}".format(treasure_in_hand[i]['name'], \
								 treasure_in_hand[i]['value']) + Color.END)

							# Select treasure to use
							to_spend = None
							while to_spend is None:
								try:
									to_spend = int(input(">> "))
									if not 0 < to_spend <= len(treasure_in_hand):
										to_spend = None
										raise ValueError
								except ValueError:
									print("Enter a valid choice")

							needed_treasure -= treasure_in_hand[to_spend-1]['value']
							treasure_used.append(treasure_in_hand.pop(to_spend-1)['name'].lower())

						# Confirm purchase and update board and player discard
						confirm = input("Confirm purchase?(y,n): ")
						if confirm == 'y':
							current_player.buy(to_buy, treasure_used)
							board.take_card(to_buy)

					else:
						print("Card not found")
				else:
					print("No buys left!")
			elif choice == 5:
				print("Undoing")
			elif choice == 6:
				print()
				break
			print()

		# Clean up
		current_player.reset_hand()
		i_play_order = 0 if i_play_order + 1 >= num_players else i_play_order + 1

		#game_done = True


class CardTypeError(Exception):
	"""
	Error type that occurs when the wrong card is used (i.e. when a player attempts
		to play a treasure card like an action card)
	"""
	def __init__(self):
		pass

if __name__ == "__main__":
    main()
