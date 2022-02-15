import msvcrt
import random
import copy
from itertools import combinations_with_replacement
import math

class Board():
    def __init__(self) -> None:
        self.board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    def getTile(self, row, col):
        return self.board[row][col]
    def setTile(self, row, col, value):
        self.board[row][col] = value
    def printBoard(self):
        print(" ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
        for row in range(0,3):
            print(f"| {self.getTile(row,0):<4} | {self.getTile(row,1):<4} | {self.getTile(row,2):<4} | {self.getTile(row,3):<4} |")
            print("|      |      |      |      |")
            print("|⎯⎯⎯⎯⎯⎯✚⎯⎯⎯⎯⎯⎯✚⎯⎯⎯⎯⎯⎯✚⎯⎯⎯⎯⎯⎯|")
        print(f"| {self.getTile(3,0):<4} | {self.getTile(3,1):<4} | {self.getTile(3,2):<4} | {self.getTile(3,3):<4} |")
        print("|      |      |      |      |")
        print(" ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
        '''
        00 | 01 | 02 | 03
        ⎯⎯⎯✚⎯⎯⎯⎯✚⎯⎯⎯✚⎯⎯⎯
        10 | 11 | 12 | 13
        ⎯⎯⎯✚⎯⎯⎯⎯✚⎯⎯⎯✚⎯⎯⎯
        20 | 21 | 22 | 23
        ⎯⎯⎯✚⎯⎯⎯⎯✚⎯⎯⎯✚⎯⎯⎯
        30 | 31 | 32 | 33

        '''

    def resetBoard(self):
        self.board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.spawnTile()
        self.spawnTile()
    
    def isLossState(self):
        # Not a loss state if there is an empty tile
        for row in self.board:
            for tileVal in row:
                if tileVal == 0:
                    return False

        copiedState = copy.deepcopy(self.board)
        
        if self.moveRight():
            self.board = copiedState
            return False
        self.board = copiedState

        
        if self.moveLeft():
            self.board = copiedState
            return False
        self.board = copiedState

        
        if self.moveUp():
            self.board = copiedState
            return False
        self.board = copiedState

        
        if self.moveDown():
            self.board = copiedState
            return False
        
        # No empty Tile and no move was possible
        self.board = copiedState
        return True

    def spawnTile(self):
        emptyTileIndecies = []
        for row in range(0,4):
            for col in range(0,4):
                if self.board[row][col] == 0:
                    emptyTileIndecies.append([row, col])
        
        if not emptyTileIndecies:
            # PLAYER LOST
            print("board is full")
            return False
        
        # Select a random place on the board
        randPos = random.choice(emptyTileIndecies)
        twoOrFour = random.randint(1,2)*2

        self.board[randPos[0]][randPos[1]] = twoOrFour
        return True

    def canSpawnTile(self):
        emptyTileIndecies = []
        for row in range(0,4):
            for col in range(0,4):
                if self.board[row][col] == 0:
                    emptyTileIndecies.append([row, col])
        
        if not emptyTileIndecies:
            # PLAYER LOST
            return False
    
        return True

    # returns whether a move was made or not
    def moveRight(self):
        moveMade = False
        for row in range(0,4):
            for col in reversed(range(0,3)): # 2 - 1 - 0
                for i in range(1, 4):
                    if col+i > 3:
                        break
                    currTileCol = col+i-1
                    nextTileCol = col+i
                    currTile = self.getTile(row, currTileCol)
                    nextTile = self.getTile(row, nextTileCol)
                    if (nextTile == 0) and not (currTile == 0 and nextTile == 0): # move as long as next tile is 0
                        self.setTile(row, nextTileCol, currTile)
                        self.setTile(row, currTileCol, 0)
                        i += 1
                        moveMade = True
                    elif (currTile == nextTile) and not (currTile == 0 and nextTile == 0): # merge two tiles
                        self.setTile(row, nextTileCol, currTile + nextTile)
                        self.setTile(row, currTileCol, 0)
                        moveMade = True
                        break
                    else:
                        break
        return moveMade

    def moveLeft(self):
        moveMade = False
        for row in range(0,4):
            for col in range(1,4): # 1 - 2 - 3
                for i in range(1, 4):
                    if col-i < 0:
                        break
                    currTileCol = col-i+1
                    nextTileCol = col-i
                    currTile = self.getTile(row, currTileCol)
                    nextTile = self.getTile(row, nextTileCol)
                    if (nextTile == 0) and not (currTile == 0 and nextTile == 0):
                        self.setTile(row, nextTileCol, currTile)
                        self.setTile(row, currTileCol, 0)
                        i += 1
                        moveMade = True
                    elif (currTile == nextTile) and not (currTile == 0 and nextTile == 0):
                        self.setTile(row, nextTileCol, currTile + nextTile)
                        self.setTile(row, currTileCol, 0)
                        moveMade = True
                        break
                    else:
                        break
        return moveMade

    def moveDown(self):
        moveMade = False
        for col in range(0,4):
            for row in reversed(range(0,3)): # 2 - 1 - 0
                for i in range(1, 4):
                    if row+i > 3:
                        break
                    currTileRow = row+i-1
                    nextTileRow = row+i
                    currTile = self.getTile(currTileRow, col)
                    nextTile = self.getTile(nextTileRow, col)
                    if (nextTile == 0) and not (currTile == 0 and nextTile == 0): # move as long as next tile is 0
                        self.setTile(nextTileRow, col, currTile)
                        self.setTile(currTileRow, col, 0)
                        i += 1
                        moveMade = True
                    elif (currTile == nextTile) and not (currTile == 0 and nextTile == 0): # merge two tiles
                        self.setTile(nextTileRow, col, currTile + nextTile)
                        self.setTile(currTileRow, col, 0)
                        moveMade = True
                        break
                    else:
                        break
        return moveMade

    def moveUp(self):
        moveMade = False
        for col in range(0,4):
            for row in range(1,4): # 1 - 2 - 3
                for i in range(1, 4):
                    if row-i < 0:
                        break
                    currTileRow = row-i+1
                    nextTileRow = row-i
                    currTile = self.getTile(currTileRow, col)
                    nextTile = self.getTile(nextTileRow, col)
                    if (nextTile == 0) and not (currTile == 0 and nextTile == 0): # move as long as next tile is 0
                        self.setTile(nextTileRow, col, currTile)
                        self.setTile(currTileRow, col, 0)
                        i += 1
                        moveMade = True
                    elif (currTile == nextTile) and not (currTile == 0 and nextTile == 0): # merge two tiles
                        self.setTile(nextTileRow, col, currTile + nextTile)
                        self.setTile(currTileRow, col, 0)
                        moveMade = True
                        break
                    else:
                        break
        return moveMade

    def makeRandomMove(self):
        randInt = random.randint(1,4)
        self.makeMoveFromInt(randInt)
    
    def makeGoodMove(self):
        # Find a good move by exploring 5 moves into the future and evaluating them with a heurisitic
        bestMove = 0
        bestMoveScore = 0

        copiedState = copy.deepcopy(self.board)
        moveSequences = combinations_with_replacement([1,2,3,4], 5) # look 5 moves in the future
        for moveSequence in moveSequences:
            self.board = copiedState # reset board
            for move in moveSequence:
               self.makeMoveFromInt(move)
            currentMoveScore = self.evaluateCurrentState()
            if currentMoveScore > bestMoveScore:
                bestMoveScore = currentMoveScore
                bestMove = moveSequence[0]
        self.board = copiedState
        self.makeMoveFromInt(bestMove)
    
    def evaluateCurrentState(self):
        # Heuristic       
        score = 0
        if self.isLossState():
            return 0

        max, secondMax = self.getMaxTile()

        if max == self.getTile(3,3): # Priorize putting the biggest tile in the bottom-right corner
            score += 40
        if secondMax == self.getTile(3,2):
            score += 20 # And the second biggest tile next to it

        score += 2 * math.log2(max) # reward bigger max tile
        score += math.log2(secondMax) # reward second biggest tile
        return score

    def basicEval(self):
        # Heuristic       
        score = 0
        if self.isLossState():
            return 0

        max, secondMax = self.getMaxTile()

        score += math.log2(max) # reward bigger max tile
        score += math.log2(secondMax) # reward second biggest tile
        return score

    def getMaxTile(self):
        max = 1
        secondMax = 1
        for row in self.board:
            for i in row:
                if i > max:
                    secondMax = max
                    max = i
        return max, secondMax

    def makeMoveFromInt(self, number):
        if number >=1 and number <= 4:
            if number==1:
                self.moveUp()
            elif number==2:
                self.moveDown()
            elif number==3:
                self.moveLeft()
            else:
                self.moveRight()
        else:
            print("ERROR: incorrect int")

"""
board = Board()

board.board = [[0,0,0,0],[0,0,0,0],[0,0,0,4],[0,0,0,1024]]
print(board.evaluateCurrentState())
board.board = [[2048,0,0,0],[0,0,0,0],[0,0,0,4],[0,0,0,8]]
print(board.evaluateCurrentState())

board.printBoard()
"""