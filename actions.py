from abc import ABC, abstractmethod
from player import Player
from board import Board
from copy import deepcopy

class Command(ABC):
	"""
	The Command interface declares a method for executing a command.
	"""

	@abstractmethod
	def execute(self) -> None:
		pass

	@abstractmethod
	def unexecute(self) -> None:
		pass

'''
# These classes are used internally and I get the feeling we only want one invoker in dominion,
#	we don't want to pass our invoker around.
class Draw(Command):
	"""
	This class describes a draw command.
	"""

	def __init__(self, player: Player, num = 1):
		self._player = player
		self.num = num

		# For unexecute
		self.old_player = deepcopy(player)

	def execute(self):
		self._player.draw(self.num)

	def unexecute(self):
		print("putting drawn card back")

class Discard(Command):
	"""
	This class describes a discard command
	"""

	def __init__(self, player: Player, to_discard: list):
		self._player = player
		self.to_discard = to_discard

		# For unexecute
		self.old_player = deepcopy(player)

	def execute(self):
		self._player.discard(self.to_discard)

	def unexecute(self):
		print("undoing discard")
'''

class Buy(Command):
	"""
	This class describes a buy command.
	"""

	def __init__(self, player: Player, board: Board, to_buy: str, treasure_used = []):
		self._board = board
		self._player = player
		self.to_buy = to_buy
		self.treasure_used = treasure_used

		# For unexecute
		self.old_player = deepcopy(player)
		self.old_board = deepcopy(board)

	def execute(self):
		self._player.buy(self.to_buy, self.treasure_used)
		self._board.take_card(self.to_buy)

	def unexecute(self):
		print("undoing buy")

class Use_action(Command):
	"""
	This class describes a use action command.
	"""

	def __init__(self, players: list, board: Board, i_current_player: int, card_name: str):
		self._players = players
		self._board = board
		self.i_current_player = i_current_player
		self.card_name = card_name

		# For unexecute
		self.old_players = deepcopy(players)
		self.old_board = deepcopy(board)

	def execute(self):
		player.use_action(self._players, self._board, self.i_current_player, self.card_name)

	def unexecute(self):
		print("undoing action")

class Reset_hand(Command):
	"""
	This class describes a reset hand command.
	"""

	def __init__(self, player: Player):
		self._player = player

		# For unexecute
		self.old_player = deepcopy(player)

	def execute(self):
		self._player.reset_hand()

	def unexecute(self):
		print("undoing buy")



class Invoker:
	"""
	The invoker has three responsibilities:
		1. Holds past commands and the states of the board and players on command creation
		2. Call the execution of commands
		3. Call the unexecution of previous commands
	"""

	def __init__(self):

		self._commands = []
		self._past_commands = []

	def set_command(self, command: Command):
		self._commands.append(command)

	def execute_commands(self):
		for i in range(len(self._commands)):
			self._commands[i].execute()
			self._past_commands.append(self._commands.pop(i))

	def set_and_execute(self, command: Command):
		self.set_command(command)
		self.execute_commands()

	def unexecute(self, num = 1):
		for i in range(num):
			self._past_commands[-1].unexecute()
			self._past_commands.pop()

