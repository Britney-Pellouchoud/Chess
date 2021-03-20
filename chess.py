

class Board(): 
	def __init__(self):
		self.winner = None	
		self.rows = 8
		self.cols = 8
		self.values = [[][][][][][][][]]
		self.whoseTurn = None

class Piece():
	def __init__(self, name, points, color):
        self.name = name
        self.name = name
        self.points = points
        self.color = color

class Pawn(Piece):
	def __init__(self, name, points, color):
		super().__init__("Pawn", 1, color)

