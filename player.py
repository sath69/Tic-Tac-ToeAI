#Player class with constructors and methods
class Player:
   def __init__(self, turn, name, isWon, symbol):
     self.turn = turn
     self.name = name
     self.isWon = isWon
     self.symbol = symbol
          
   def check(self, gameUI):
       #check row
       for x in range(len(gameUI)):
          rowSet = set(gameUI[x])
          if len(rowSet) == 1 and self.symbol in rowSet:
             self.isWon = True
       
       #check column
       for x in range(len(gameUI)):
         columnSet = set()
         for i in range(len(gameUI[x])):
          columnSet.add(gameUI[i][x])
         if len(columnSet) == 1 and self.symbol in columnSet:
             self.isWon = True

       #Diagonal
       leftDiagonalSet = set()
       rightDiagonalSet = set()

       #check left diagonal
       for x in range(len(gameUI)):
          leftDiagonalSet.add(gameUI[x][x])
       if len(leftDiagonalSet) == 1 and self.symbol in leftDiagonalSet:
          self.isWon = True
      
       #check right diagonal
       for x in range(len(gameUI)):
        rightDiagonalSet.add(gameUI[x][len(gameUI) - 1 - x])
       if len(rightDiagonalSet) == 1 and self.symbol in rightDiagonalSet:
          self.isWon = True
   
   def pick(self, gameUI, row, column):
      
      isPicked = False
      try:
       if gameUI[row-1][column-1] == "X" or gameUI[row-1][column-1] == "O":
          print("\nThat area has been already filled, please select another row and column.")
          return isPicked
       else:
         gameUI[row-1][column-1] = self.symbol
         isPicked = True
         return isPicked
      except Exception:
          print("\nYou must pick a row and column number between 1 and 3")
          return isPicked
