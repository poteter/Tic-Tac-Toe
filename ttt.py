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
    
    def check4winner(self):
        pass

    def checkPlayerState(self, playerstate):
        if playerstate == 0:
             self.xo = "x" 
        elif playerstate == 1:
               self.xo = "o"

    
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


    def start(self):
        self.logic()
    
    def endscreen(self):
        self.checkPlayerState(self.playerstate)

        print("######################")
        print("##     {} WINS!     ##".format(self.xo))
        print("######################")

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
