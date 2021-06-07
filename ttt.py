#! usr/bin/python

# TicTacToe

class game:
    def __init__(self):
        self.playerstate = 0
        self.xo = "x"
        self.coords = {"x":[], "o":[]}
        self.winpatterns = {1:["A1","B1","C1"], 2:["A2","B2","C2"], 3:["A3","B3","C3"], 
                            4:["A1","A2","A3"], 5:["B1","B2","B3"], 6:["C1","C2","C3"], 
                            7:["A1","B2","C3"], 8:["A3","B2","C1"]}
        self.gamestate = 0
        self.tempinput = ""
    
    # takes the coords dict and the winpatterns dict and checks for matching patterns
    # if a matching pattern is found, changes gamestate to 1 ending the infinite loop.
    def check4winner(self):
        pass
    
    # takes in the playerstate variable and changes the player symbol to either 
    # x or o.
    def checkPlayerState(self, playerstate):
        if playerstate == 0:
             self.xo = "x" 
        elif playerstate == 1:
               self.xo = "o"

    # the game logic, starts the infinite loop, and runs the game mechanics.
    def logic(self):
        while self.gamestate == 0:
            self.drawboard()
            if self.playerstate == 0:
                self.tempinput = input()
                self.coords["x"].append(self.tempinput)
            elif self.playerstate == 1:
                self.tempinput = input()
                self.coords["o"].append(self.tempinput)
            
            self.endscreen()
            self.gamestate = 1

    # used to start the game by calling the logic method.
    def start(self):
        self.logic()
    
    # draws the win screen and displays the winner.
    def endscreen(self):
        self.checkPlayerState(self.playerstate)

        print("######################")
        print("##     {} WINS!     ##".format(self.xo))
        print("######################")

    # draws the game board, and displays the current player.
    def drawboard(self):
        self.checkPlayerState(self.playerstate)

        print("\n\n### TicTacToe ###\n\n")
        print("    A   B   C  ")
        print("  +---+---+---+")
        print(" 1|   |   |   |")
        print("  +---+---+---+")
        print(" 2|   |   |   |")
        print("  +---+---+---+")
        print(" 3|   |   |   |")
        print("  +---+---+---+")
        print("\n =================")
        print(" player : {}".format(self.xo))
        print(" enter choice...")
        print(" =================")
g = game()
g.start()
