import tkinter as tk
from player import Player  
from PIL import Image, ImageTk

#Main Game Loop with the graphical user interface code

class Game:
    def __init__(self, turnCounter, grid):
        self.turnCounter = turnCounter
        self.gameUI = grid
        self.player1 = Player(0, "Cross (X)", False, "X")  
        self.player2 = Player(1, "Nought (O)", False, "O")
        self.root = tk.Tk()
        x_image = Image.open("C:/Users/User/OneDrive/Desktop/Tic-Tac-Toe/Graphics/cross.png").resize((150, 150)) # Modify this path to the files where the graphics are
        o_image = Image.open("C:/Users/User/OneDrive/Desktop/Tic-Tac-Toe/Graphics/nought.png").resize((205, 205)) # Modify this path to the files where the graphics are
        self.x_image = ImageTk.PhotoImage(x_image)
        self.o_image = ImageTk.PhotoImage(o_image)
        self.status = tk.Label(self.root, text="Player Status", font=("Helvetica", 17))
    def OnTriggerEvent(self, label, row, column):
        self.turn()
        if self.turnCounter % 2 == 0:
            self.player1.pick(self.gameUI, row, column)
            label.config(image=self.x_image) 
            self.player1.check(self.gameUI)
            self.turnCounter += 1
        else:
            self.player2.pick(self.gameUI, row, column)
            label.config(image=self.o_image)
            self.player2.check(self.gameUI)
            self.turnCounter += 1

        if self.player1.isWon:
            self.player1.won()
            win2 = tk.Label(self.root, text= f"\n{self.player1.name} won the game!", font=("Helvetica", 11), foreground="blue")
            win2.grid(row=0, column=0, columnspan=1, pady=20)
            self.disable()
            self.status.config(text="")
            return
        elif self.player2.isWon:
            self.player2.won()
            win1 = tk.Label(self.root, text=f"\n{self.player2.name} won the game!", font=("Helvetica", 11), foreground="blue")
            win1.grid(row=0, column=0, columnspan=1, pady=20)
            self.disable()
            self.status.config(text="")
            return
        elif all("-" not in row for row in self.gameUI):
            draw = tk.Label(self.root, text= "Draw!", font=("Helvetica", 11),foreground="red")
            draw.grid(row=0, column=0, columnspan=1, pady=20)
            self.disable()
            self.status.config(text="")
            return
        self.turn()
    def turn(self):
     
     self.status.grid(row=0, column=2, columnspan=4, pady=20)
     if self.turnCounter % 2 == 0:
        self.status.config(text=f"{self.player1.name}'s turn")
     else:
        self.status.config(text=f"{self.player2.name}'s turn")

    def game(self):
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("900x900")
        self.root.resizable(False, False) 

        img = tk.PhotoImage(file="C:/Users/User/OneDrive/Desktop/Tic-Tac-Toe/Graphics/icon_tictactoe.png")  # Modify this path to the files where the graphics are
        self.root.iconphoto(False, img) 

        title_label = tk.Label(self.root, text="Tic Tac Toe", font=("Helvetica", 24))
        title_label.grid(row=0, column=0, columnspan=3, pady=20)

        self.turn()

        self.label = tk.Button(self.root, text="" ,command=lambda: self.OnTriggerEvent(self.label, 1, 1))
        self.label2 = tk.Button(self.root, text="", command=lambda: self.OnTriggerEvent(self.label2, 1, 2))
        self.label3 = tk.Button(self.root, text="", command=lambda: self.OnTriggerEvent(self.label3, 1, 3))
        self.label4 = tk.Button(self.root, text="",  command=lambda: self.OnTriggerEvent(self.label4, 2, 1))
        self.label5 = tk.Button(self.root, text="",  command=lambda: self.OnTriggerEvent(self.label5, 2, 2))
        self.label6 = tk.Button(self.root, text="", command=lambda: self.OnTriggerEvent(self.label6, 2, 3))
        self.label7 = tk.Button(self.root, text="", command=lambda: self.OnTriggerEvent(self.label7, 3, 1))
        self.label8 = tk.Button(self.root, text="",  command=lambda: self.OnTriggerEvent(self.label8, 3, 2))
        self.label9 = tk.Button(self.root, text="", command=lambda: self.OnTriggerEvent(self.label9, 3, 3))

        self.root.columnconfigure(0, weight=1, minsize=210)
        self.root.columnconfigure(1, weight=1, minsize=210)
        self.root.columnconfigure(2, weight=1, minsize=210)
        self.root.rowconfigure(1, weight=1, minsize=210)
        self.root.rowconfigure(2, weight=1, minsize=210)
        self.root.rowconfigure(3, weight=1, minsize=210) 

        self.label.grid(row=1, column=0, sticky="nesw")
        self.label2.grid(row=1, column=1, sticky="nesw")
        self.label3.grid(row=1, column=2, sticky="nesw")
        self.label4.grid(row=2, column=0, sticky="nesw")
        self.label5.grid(row=2, column=1, sticky="nesw")
        self.label6.grid(row=2, column=2, sticky="nesw")
        self.label7.grid(row=3, column=0, sticky="nesw")
        self.label8.grid(row=3, column=1, sticky="nesw")
        self.label9.grid(row=3, column=2, sticky="nesw")

        self.root.mainloop()
    def disable(self):
        self.label["state"] = tk.DISABLED
        self.label2["state"] = tk.DISABLED
        self.label3["state"] = tk.DISABLED
        self.label4["state"] = tk.DISABLED
        self.label5["state"] = tk.DISABLED
        self.label6["state"] = tk.DISABLED
        self.label7["state"] = tk.DISABLED
        self.label8["state"] = tk.DISABLED
        self.label9["state"] = tk.DISABLED

        
game = Game(0, [["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"]])
game.game()
