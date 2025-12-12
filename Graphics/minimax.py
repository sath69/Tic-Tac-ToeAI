import math
import copy

class Minimax:

 #Loops through the gameboard for empty positions and assign them temporarily
 #returns a position to be assigned to the game board
 def makeMove(self, board):
    value = -math.inf
    position = 0
    for x in range(len(board)):
       for y in range(len(board)):  
        if board[x][y] == "-":
            board[x][y] = "O" #Apply move
            score = self.minimaxFunc(board, 0) #This is recursed throughout the whole 
            board[x][y] = "-" #Undo move 
            if score > value:
                 value = score
                 position = (x,y)
    return position

 def minimaxFunc(self, board, turn,alpha=-math.inf,beta=math.inf,):
   
   #Terminal states to check if AI or Human won or if they both draw
   if self.checkTerminalState(board, "O") == True:
        return 1
   if self.checkTerminalState(board, "X") == True:
        return -1
   elif all("-" not in row for row in board):  
        return 0
  
   #This is for maximising for the AI (Player 2)
   if turn == 1:
        value = -math.inf
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == "-":
                    board[x][y] = "O"
                    value = max(value, self.minimaxFunc(board, 0, alpha, beta))
                    board[x][y] = "-"
                    alpha = max(alpha, value)
                    if beta <= alpha:  
                        return value
        return value

   #This is minimising for Human (Player 1)
   if turn == 0:
       value = math.inf
       for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == "-":
                     board[x][y] = "X"
                     value = min(value, self.minimaxFunc(board, 1, alpha, beta))
                     board[x][y] = "-"
                     beta = min(beta, value)
                     if beta <= alpha:  
                        return value
       return value                

 #Same logic but its for the replica board
 def checkTerminalState(self, gameUI, symbol):
    
     #check row
       for x in range(len(gameUI)):
          rowSet = set(gameUI[x])
          if len(rowSet) == 1 and symbol in rowSet:
             return True
       
       #check column
       for x in range(len(gameUI)):
         columnSet = set()
         for i in range(len(gameUI[x])):
          columnSet.add(gameUI[i][x])
         if len(columnSet) == 1 and symbol in columnSet:
             return True

       #Diagonal
       leftDiagonalSet = set()
       rightDiagonalSet = set()

       #check left diagonal
       for x in range(len(gameUI)):
          leftDiagonalSet.add(gameUI[x][x])
       if len(leftDiagonalSet) == 1 and symbol in leftDiagonalSet:
            return True
      
       #check right diagonal
       for x in range(len(gameUI)):
        rightDiagonalSet.add(gameUI[x][len(gameUI) - 1 - x])
       if len(rightDiagonalSet) == 1 and symbol in rightDiagonalSet:
           return True
