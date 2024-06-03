import random
com_score=0
y_score=0

lst=['r','p','s']
#Checking and changing value of scores
def check(human,computer):
    #p>r,s>p,r>s
    global y_score
    global com_score

    if (human == 'p' and computer =='r') or (human == 's' and computer =='p') or \
        (human == 'p' and computer =='r'):
        print("You won")
        y_score+=1
    else:
        print("You lost")
        com_score+=1
    return


#Rock Paper Scissor
def rps(chances):
    
    while chances>0:
        computer=random.choice(lst)
        human=input("Enter your choice\n")
        chances-=1
        if(human != computer):
            check(human,computer)
        else:
            print("Tie")
    
    

#Main
chances=int(input("Enter number of times you want to play\n"))

rps(chances)

if (com_score > y_score):
    print("Computer WON the game !!\n")
elif (y_score > com_score):
    print("You WON the game!!\n")
else :
    print("It's a TIE !!")

