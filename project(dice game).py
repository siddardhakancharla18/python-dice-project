#DICE GAME
import random
def roll():
    n=random.randint(1,6)
    return n
players=eval(input("enter the no.of players(2-4):"))
score=0
x=[]
y=[]
n=0
w=0
p=0
q=0
t=0
tu=0
f=input("press enter:")
for i in range(1,players+1):
    print("chance of player",i,":")
    while True:
        c=roll()
        p=p+1
        g=input("if you are ready to roll then press yes(y):")
        if(g=='y' and c!=1):
            print("you rolled:",c)
            score=score+c
        elif(c==1):
            print("you rolled 1.so it's time to exit!")
            print("")
            s=score-n
            z=p-q
            print("SCORE OF THE PLAYER",i,"IS ",s,"  IN  ",z," ROLLS")
            q=p
            n=score
            print("\n--------------------------------------------------")
            if(s>=30):
                    x.append(z)
                    if(z==min(x)):
                        t=i
                        tu=1
            else:
                y.append(s)
    
                w=max(y)
                tw=i
            break
if(tu==1):
    print("WINNER OF THIS GAME IS:PLAYER",t)
else:
    print(tw)
