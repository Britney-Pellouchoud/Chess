#make a tic tac toe game

import time
import random


class Board():

	
	
	def __init__(self):
		self.winner = None	
		self.rows = 2
		self.cols = 2
		self.values = [["", "", ""],["", "", ""],["", "", ""]]
		self.playerSymbol = None
		self.AISymbol = None
		self.whoseTurn = None

	def setPlayerSymbol(self, symbol):
		self.playerSymbol = symbol
		if self.playerSymbol == "X":
			self.AISymbol = "O"
		else:
			self.AISymbol = "X"

	def isOccupied(self, x, y):
		if self.values[x][y]:
			return True
		return False

	
	def placeMove(self, x, y, z):
		self.values[x][y] = z

	def isEmpty(self):
		if self.values == [["", "", ""],["", "", ""],["", "", ""]]:
			return True
		return False
		

	def AIMakeMove(self):

		bestMove = None
		bestScore = 0

		if self.isEmpty():
			bestMove = [1, 1]

		i = 0
		j = 0
		while i <= self.rows:
			j = 0
			while j <= self.cols:
				if not self.isOccupied(i, j):
					score = self.estimateScore(i, j)
					if score > bestScore:
						bestScore = score
						bestMove = [i, j]
				j += 1
			i += 1


		return self.placeMove(bestMove[0], bestMove[1], self.AISymbol)

	
		
	#because of the way AIMakeMove is structured, estimateScore will only receive open spots

	def estimateScore(self, i, j):
		possibleWins = [
		[[0, 0], [1, 1], [2,2]], #d1
		[[0, 2], [1, 1], [2,0]],#d2

		[[0, 0], [0, 1], [0,2]], #r1
		[[1, 0], [1, 1], [1,2]], #r2
		[[2, 0], [2, 1], [2,2]], #r3

		[[0, 0], [1, 0], [2,0]], #c1
		[[0, 1], [1, 1], [2,1]], #c2
		[[0, 2], [1, 2], [2,2]] #c3
		]

		if i == 1 and j == 1:
			return 3


		
		#if you could win, make the move that wins
		#if the opponent could win next round, stop them

		for win in possibleWins:
			otherSpots = [spot for spot in win if spot != [i, j]]
			if len(otherSpots) == 2:
				spot1 = otherSpots[0]
				spot2 = otherSpots[1]
				if self.values[spot1[0]][spot1[1]] == self.values[spot2[0]][spot2[1]]:
					if not self.values[spot1[0]][spot1[1]]:
						return 1
					elif self.values[spot1[0]][spot1[1]] == self.AISymbol:
						return 11
					else:
						return 10

		return 1


	def checkIfFinished(self):
		i = 0
		while i <= 2:
			#column win
			if self.values[0][i] == self.values[1][i] and self.values[1][i] ==  self.values[2][i]:
				
				if not self.values[0][i]:
					return False
				print("HITS HERE 1")
				if self.values[0][i] == self.AISymbol:
					self.winner = "I"
				else:
					self.winner = "You"
				return True
			#row win
			if self.values[i][0] == self.values[i][1] and self.values[i][1] == self.values[i][2]:
				if not self.values[i][0]:
					return False
				print("HITS HERE 2")
				if self.values[i][0] == self.AISymbol:
					self.winner = "I"
				else:
					self.winner = "You"
				return True
			i += 1

		#diagonal win d1
		if self.values[0][0] == self.values[1][1] and self.values[1][1] == self.values[2][2]:
			if not self.values[0][0]:
				return False
			print("HITS HERE 3")
			if self.values[0][0] == self.AISymbol:
				winner = "I"
			else:
				winner = "You"
			return True

		#diagonal win d2
		elif self.values[2][0] == self.values[1][1] and self.values[1][1] == self.values[0][2]:
			if not self.values[0][2]:
				return False
			print("HITS HERE 4")
			if self.values[1][1] == self.AISymbol:
				winner = "I"
			else:
				winner = "You"
			return True

		#it is a draw
		elif self.isDraw():
			winner = "No one"
			return True


		else:
			return False

	
	def isDraw(self):
		i = 0
		j = 0
		while i < 2:
			j = 0
			while j < 2:
				if self.values[i][j]:
					return False
				j += 1
			i += 1

		return True




	def printBoard(self):
		for i in self.values:
			print(i)




def start():
	board = Board()
	board.printBoard()
	playerSymbol = input("Would you like to be 'X' or 'O' ? (Please use capital letters.)")
	board.setPlayerSymbol(playerSymbol)

	print("Okay!  Let's do a coin toss!  Heads I go first, tails you go first.")
	time.sleep(2)
	print("Flipping coin...")
	print("...")
	time.sleep(2)
	val = random.randint(1, 11)

	if val > 5:
		print("Okay!  You go first.")
		board.whoseTurn = 0

	else:
		print("Okay!  I go first.")
		board.whoseTurn = 1

	

	#0 is opponent
	#1 is player
	while not board.checkIfFinished():


		if board.whoseTurn == 0:
			x = int(input("Where do you want to mark next? [X value]"))
			y = int(input("Where do you want to mark next? [Y value]"))
			if x not in [0, 1, 2]:
				print("Sorry!  This spot is out of bounds, try another.")
				continue
			if board.isOccupied(x, y):
				print("Sorry!  This spot is already occupied, try another.")
				continue
			

			else:
				board.placeMove(int(x), int(y), board.playerSymbol)
				board.whoseTurn = 1
				board.printBoard()
				continue

		else:
			print("Let me think...")

			time.sleep(2)
			board.AIMakeMove()

			board.whoseTurn = 0
			board.printBoard()
		
		board.checkIfFinished()
		
	
	board.printBoard()
	print(board.winner + " won.  Game over.")









start()






