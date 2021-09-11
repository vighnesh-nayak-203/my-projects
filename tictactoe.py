from os import system
from time import sleep
class player:
    def __init__(self,name,symbol):
        self.name=name
        self.sym=symbol
        self.point=0
class game:
    def __init__(self,p1,p2):
        self.board=[None]
        self.p1=p1
        self.p2=p2
        self.winner=None
        self.move=0
        self.combos=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        for i in range(9):
            self.board.append(" ")
    def wincheck(self):
        for i in self.combos:
            if self.board[i[0]]==self.board[i[1]] and self.board[i[0]]==self.board[i[2]] and self.board[i[0]]!=" ":
                if self.board[i[0]]==self.p1.sym:
                    self.winner=self.p1
                else:
                    self.winner=self.p2
                self.endgame()
                break
    def endgame(self):
        self.move=9
        system('cls')
        self.prnt()
        if self.winner!=None:
            self.winner.point+=1
            print(f"{self.winner.name} won this Game.")
        else:
            print("This game is a draw.")
        print("End of the Game.Thank You.")
    def prnt(self):
        print("\n-------")
        for i in range(3):
            print("|",end="")
            for j in range(3):
                a=(3*i)+1+j
                print(self.board[a],end="|")
            print("\n-------")
    def play(self):
        curr_player=self.p1
        while self.move<9:
            system('cls')
            self.prnt()
            crt=False
            while not crt:
                inp=int(input(f"{curr_player.name} enter your place:"))
                if inp<=9 and inp>=1:
                    if self.board[inp]==" ":
                        crt=True
                    else:
                        print("Place occupied.")
                else:
                    print("Place does not exist. Please enter a value between 1-9.")
            self.board[inp]=curr_player.sym
            self.wincheck()
            self.move+=1
            if curr_player!=self.p1:
                curr_player=self.p1
            else:
                curr_player=self.p2
def main():
    n1=str(input("Enter player-1 name:"))
    s1=str(input("Enter player-1 symbol:"))
    n2=str(input("Enter player-2 name:"))
    s2=str(input("Enter player-2 symbol:"))
    p1=player(n1,s1)
    p2=player(n2,s2)
    again=True
    while again:
        print("The Game starts now.")
        sleep(2)
        a=game(p1,p2)
        a.play()
        b=str(input("Do you want to play again?(Y/N)")).upper()
        if b!="Y":
            again=False
    if p1.point>p2.point:
        print(f"This session is won by {p1.name} against {p2.name} by {p1.point}-{p2.point}.")
    elif p1.point<p2.point:
        print(f"This session is won by {p2.name} against {p1.name} by {p2.point}-{p1.point}.")
    else:
        print(f"This session is a draw between {p1.name} and {p2.name} by {p1.point}-{p2.point}.")
if __name__=="__main__":
    main()