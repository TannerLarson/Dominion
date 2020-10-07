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


class Draw(Command):

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

	def __init__(self, player: Player, to_discard: list):
		self._player = player
		self.to_discard = to_discard

		# For unexecute
		self.old_player = deepcopy(player)

	def execute(self):
		self._player.discard(self.to_discard)

	def unexecute(self):
		print("undoing discard")

class Buy(Command):

	def __init__(self, player: Player, to_buy: str, treasure_used = []):
		self._player = player
		self.to_buy = to_buy
		self.treasure_used = treasure_used

		# For unexecute
		self.old_player = deepcopy(player)

	def execute(self):
		self._player.buy(self.to_buy, self.treasure_used)

	def unexecute(self):
		print("undoing buy")

class Use_action(Command):

	def __init__(self, player: Player, board: Board, card_name: str, other_players: list):
		self._player = player
		self._board = board
		self._other_players = other_players
		self.card_name = card_name

		# For unexecute
		self.old_player = deepcopy(player)
		self.old_board = deepcopy(board)
		self.old_other_players = deepcopy(other_players)

	def execute(self):
		self._player.use_action(self.card_name, self._other_players, self._board)

	def unexecute(self):
		print("undoing action")

class Reset_hand(Command):

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
	Ask the command to carry out the request
	"""

	def __init__(self):

		self._commands = []

	def set_command(self, command):
		self._commands.append(command)

	def exectue_commands(self):
		for command in self._commands:
			command.execute()