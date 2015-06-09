###############################################
# hw8c.py
###############################################
# Ida Chow + Section Q + Andrew ID: ichow
# (Collaborated with Angela Qiu, Andrew ID: aqiu)
###############################################

# TetrisClassAnimation.py

# Adapted from: tetris8.py from here:
# http://www.kosbie.net/cmu/fall-10/15-110/handouts/tetris/tetris.html


import random
import copy
from Tkinter import *
from basicAnimationClass import BasicAnimationClass

class TetrisClassAnimation(BasicAnimationClass):
	def __init__(self, rows, cols):
		margin = 40
		cellSize = 20
		self.canvasWidth = canvasWidth = 2*margin + cols*cellSize
		self.canvasHeight = canvasHeight = 2*margin + rows*cellSize
		super(TetrisClassAnimation, self).__init__(canvasWidth, canvasHeight)
		self.margin = margin
		self.cellSize = cellSize
		self.rows = rows
		self.cols = cols
		self.boardColor = "blue"
		self.score = 0
		self.tetrisBoard = [[self.boardColor for x in xrange(cols)] 
						for x in xrange(rows)] 
		self.initPieces()



	####### stored data  

	def initPieces(self):
		#Seven "standard" pieces (tetrominoes)
		  self.iPiece = [[ True,  True,  True,  True]]
		  self.jPiece = [[ True, False, False ],[ True, True,  True]]
		  self.lPiece = [[ False, False, True],[ True,  True,  True]]
		  self.oPiece = [[ True, True],[ True, True]]		  
		  self.sPiece = [[ False, True, True],[ True,  True, False ]]
		  self.tPiece = [[ False, True, False ],[ True,  True, True]]
		  self.zPiece = [[ True,  True, False ],[ False, True, True]]

		  self.tetrisPieces = [self.iPiece, self.jPiece, 
		  					self.lPiece, self.oPiece, self.sPiece, 
		  					self.tPiece, self.zPiece]

		  self.tetrisPieceColors = [ "red", "yellow", "magenta",
		  						 "pink", "cyan", "green", "orange" ]


	######  copy function

	def myDeepCopy(self,a):
	    if (isinstance(a, list) or isinstance(a, tuple)):
	        return [self.myDeepCopy(element) for element in a]
	    else:
	        return copy.copy(a)

	####### player controls

	def onKeyPressed(self, event): 
		self.ignoreNextTimerEvent = True # for better timing
		# first process keys that work even if the game is over
		if (event.char == "q"):   self.gameOver()
		elif (event.char == "r"): self.initAnimation()
		elif (event.char == "d"): self.inDebugMode = not self.inDebugMode
		# now process keys that only work if the game is not over
		if (self.isGameOver == False):
			if (event.keysym == "Down"):  self.moveFallingPiece(+1, 0)
			elif (event.keysym == "Left"):  self.moveFallingPiece(0,-1)
			elif (event.keysym == "Right"): self.moveFallingPiece(0,+1)		
			elif (event.keysym == "Up"): self.rotateFallingPiece()





	##### game piece functionalities

	def newFallingPiece(self):
		# new falling piece random, with color
		self.rand = rand = random.randint(0,6)
		self.newPiece = self.tetrisPieces[rand]
		self.newColor = self.tetrisPieceColors[rand]
		self.currentRow = 0
		self.currentCol = (self.cols/2) - (len(self.newPiece[0])/2)
		# print rand, self.newColor, self.currentRow, self.currentColumn



	def moveFallingPiece(self,dRow,dCol):
		self.moved = True
		self.currentRow += dRow
		self.currentCol += dCol
		if (self.fallingPieceIsLegal() == False):
			self.currentRow -= dRow
			self.currentCol -= dCol
			self.moved = False

	def fallingPieceIsLegal(self):
		legal = True
		# check if falling piece is ON BOARD
		for row in xrange(self.currentRow,self.currentRow+len(self.newPiece)):
			for col in xrange(self.currentCol,self.currentCol+len(self.newPiece[0])):
				if self.newPiece[row - self.currentRow][col - self.currentCol] == True:
					if not(0 <= row < self.rows): 
						legal = False

					if not(0 <= col < self.cols): 
						legal = False
					if legal == True:
						# check if falling piece is ON BOARD THAT IS BACKGROUND
						if self.tetrisBoard[row][col] != self.boardColor:
							legal = False
		return legal



	def rotateFallingPiece(self):
		numOfCols = len(self.newPiece)
		numOfRows = len(self.newPiece[0])
		down = 0

		save = self.newPiece
		oldCenterRow, oldCenterCol = self.fallingPieceCenter()

		rotatedPiece = [[0 for x in xrange(numOfCols)] for x in xrange(numOfRows)]
		for row in xrange(len(rotatedPiece)):
			for col in xrange(len(rotatedPiece[0])):
				rotatedPiece[row][col] = self.newPiece[down][numOfRows - row - 1]
				down += 1
				if down == numOfCols: down = 0
		
		self.newPiece = rotatedPiece

		newCenterRow, newCenterCol = self.fallingPieceCenter()

		self.currentRow += oldCenterRow - newCenterRow
		self.currentCol += oldCenterCol - newCenterCol

		if (self.fallingPieceIsLegal() == False):
			self.currentRow -= oldCenterRow - newCenterRow
			self.currentCol -= oldCenterCol - newCenterCol
			self.newPiece = save


		
	def fallingPieceCenter(self):
		rows = len(self.newPiece)
		cols = len(self.newPiece[0])
		rowAndCol = self.currentRow + rows/2, self.currentCol + cols/2
		return rowAndCol


	def placeFallingPiece(self):
		tetrisBoard = self.tetrisBoard
		rows = len(tetrisBoard)
		cols = len(tetrisBoard[0])


		for row in xrange(self.currentRow,self.currentRow+len(self.newPiece)):
			for col in xrange(self.currentCol,self.currentCol+len(self.newPiece[0])):			
				if self.newPiece[row - self.currentRow][col - self.currentCol] == True: 
					self.tetrisBoard[row][col] = self.newColor
				# else: 
				# 	self.tetrisBoard[row][col] = ""

		self.removeFullRows()




	##### remove rows

	def removeFullRows(self): 
		board = self.myDeepCopy(self.tetrisBoard)
		numOfRows = len(self.tetrisBoard)
		numOfCols = len(self.tetrisBoard[0])
		oldRow = [0 for x in xrange(numOfCols)] 
		blanks = removed = 0
		newRow = numOfRows - 1
		
		for row in xrange(numOfRows-1,0,-1):
			oldRow = [0 for x in xrange(numOfCols)] 
			blanks = 0
			for col in xrange(numOfCols):
				if self.tetrisBoard[row][col] == self.boardColor:
					blanks += 1
				oldRow[col] = self.tetrisBoard[row][col]
			if blanks > 0:
				board[newRow] = copy.copy(oldRow)
				newRow -= 1
			else: removed += 1

		self.score += removed**2
		self.tetrisBoard = board
		print self.score



	##### other game stuff


	def gameOver(self):
		self.isGameOver = True

	##### timer things

	def onTimerFired(self):
		if (self.isGameOver == False):
			ignoreThisTimerEvent = self.ignoreNextTimerEvent
			self.ignoreNextTimerEvent = False
			self.loadTetrisBoard()
			self.moveFallingPiece(+1, 0)
			if self.moved == False:
				self.placeFallingPiece()
				self.newFallingPiece()

				if self.fallingPieceIsLegal() == False:
					self.isGameOver = True

	##### drawing!!!!

	def drawInstructions(self):
		self.canvas.create_text(self.width/2,self.height - 20, 
								text="LEFT/RIGHT/DOWN to move tetris piece. UP to rotate.",
								 font=("Helvetica",8), fill="black")

	def redrawAll(self):
		self.canvas.delete(ALL)
		self.canvas.create_rectangle(0,0,self.canvasWidth,self.canvasHeight,fill="orange")
		self.drawTetrisBoard()
		self.drawFallingPiece()
		self.drawInstructions()
		if (self.isGameOver == True):
			cx = self.width/2
			cy = self.height/2
			self.canvas.create_text(cx, cy, text="Game Over!", font=("Helvetica", 32, "bold"), fill="yellow")
		self.canvas.create_text(40,20, text="Score: ", font=("Helvetica",10), fill="black")
		self.canvas.create_text(75,20, text=self.score, font=("Helvetica",10), fill="black")

	def drawTetrisBoard(self):
		# draw the board (which includes fallen pieces)
		tetrisBoard = self.tetrisBoard
		rows = len(tetrisBoard)
		cols = len(tetrisBoard[0])
		
		for row in xrange(rows):
			for col in xrange(cols):
				self.drawTetrisCell(row,col,tetrisBoard[row][col])


	def drawTetrisCell(self,row,col,color):
		# draw the falling pieces

		tetrisBoard = self.tetrisBoard

		margin = self.margin
		cellSize = self.cellSize
		left = margin
		top = margin

		# draws color that is manipulated in other places.... for falling pieces
		self.canvas.create_rectangle(left + col * cellSize, 
											top + row * cellSize, 
											left + col * cellSize + cellSize, 
											top + row * cellSize + cellSize, 
											fill=color, width="4")



	def drawFallingPiece(self):
		tetrisBoard = self.tetrisBoard
		rows = len(tetrisBoard)
		cols = len(tetrisBoard[0])


		for row in xrange(self.currentRow,self.currentRow+len(self.newPiece)):
			for col in xrange(self.currentCol,self.currentCol+len(self.newPiece[0])):
								

				if self.newPiece[row - self.currentRow][col - self.currentCol] == True:
																color = self.newColor
				else: color = ""
				self.drawTetrisCell(row,col,color)


	##### tetris board calibration & things

	def calcBoard(self):
		tetrisBoard = self.tetrisBoard
		rows = self.rows
		cols = self.cols

		# place current piece 
		for row in range(rows): 
			for col in range(cols):
				tetrisBoard[row][col] = self.boardColor


	def loadTetrisBoard(self):
		tetrisBoard = self.tetrisBoard
		rows = self.rows
		cols = self.cols


	##### some more init stuff

	def initAnimation(self):
		self.loadTetrisBoard()
		self.inDebugMode = False
		self.isGameOver = False
		self.tetrisDrow = 0
		self.tetrisDcol = -1 # start moving left
		self.ignoreNextTimerEvent = False
		self.app.setTimerDelay(500)

		self.newFallingPiece()

TetrisClassAnimation(15, 10).run()