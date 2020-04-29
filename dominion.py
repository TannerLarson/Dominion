import cards
import random 

class Board():

	def __init__(self, num_players):
		self.num_estates
		self.num_dutchies
		self.num_provinces
		self.num_curses
		self.num_copper
		self.num_silver
		self.num_gold
		self.action_cards = {}

class Player():

	def __init__(self):
		self.discard_pile = []
		self.draw_pile = random.sample(['c','c','c','c','c','c','c','e','e','e'], 10)
		self.num_actions = 1
		self.num_buys = 1
		self.hand = self.draw_pile[:5]

	def shuffle_deck():
		pass

	def draw(num = 1):
		if len(draw_pile) < num:
			temp = draw_pile[:num]
			shuffle_deck()
			draw_pile.insert(0, temp)
		self.hand = self.draw_pile[:num]
		self.draw_pile = self.draw_pile[num:]

	def buy():
		pass


def main():
    num_players = int(input("Number of players: "))
    if num_players < 2:
    	print("Not enough players")
    	return
    players = [Player() for x in range(0, num_players)]
    print(players[0].hand)

if __name__ == "__main__":
    main()
