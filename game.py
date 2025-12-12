#AI TicTacToe using Minimax algorithm, player must input a row and column (1-3).
#I can't do GUI because I cant be asked, I already made my own GUI version previously.

from minimax import Minimax
from player import Player

class Game:
    def __init__(self, turnCounter, grid):
        self.turnCounter = turnCounter
        self.gameUI = grid

    def game(self):
        
        #Main game loop

        #Initialise players
        p1 = Player(1, "Cross (X)", False, "X")
        p2 = Player(0, "Nought (O)", False, "O")

        #Intiailise minimax algorithm
        minimax = Minimax()
        
        while True:
            
            self.updateBoard()

            #For "X"
            if self.turnCounter % 2 != 0:
                print(f"{p1.name}'s turn")
                row = int(input("Enter row (1-3): "))
                col = int(input("Enter column (1-3): "))
                if p1.pick(self.gameUI, row, col) == False:
                     continue
                p1.check(self.gameUI)
                if p1.isWon:
                    self.updateBoard()
                    print(f"{p1.name} has won the game!")
                    exit()
                self.turnCounter += 1
            
            #For "O"
            else:
                print(f"{p2.name}'s turn (AI)")
                move = minimax.makeMove(self.gameUI)
                x, y = move
                self.gameUI[x][y] = p2.symbol
                print(f"AI picks: {x+1}, {y+1}")
                p2.check(self.gameUI)
                if p2.isWon:
                    self.updateBoard()
                    print(f"{p2.name} has won the game!")
                    exit()
                self.turnCounter += 1
             
            if all("-" not in r for r in self.gameUI):
                self.updateBoard()
                print("It is a draw!")
                exit()
            
    #Gives an updated version of the board
    def updateBoard(self):
        for row in self.gameUI:
            print("".join(row))
        print()

#Game Initialisation
game = Game(1, [["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"]])
game.game()
