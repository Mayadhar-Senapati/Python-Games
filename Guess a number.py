import random
def guess_by_user(x):
    score=10
    guess_num=random.randint(1,x)
    my_num=0
    while my_num != guess_num and score>0:
        my_num=int(input(f"Enter your number :   \t\t Chances left are : {score}\n" ))
        
        if my_num>guess_num:
            print("Entered value is too High ")
            score-=1
        elif my_num<guess_num:

            print("Entered value is too Low ")
            score-=1
    
    if score>0:
        print(f"Hurray ! You found the number {guess_num}  and your SCORE is {score}\n\n")
        return
    elif score<=0:
        print("Chances exceeded!! TRY AGAIN!!\n\n")
        return

    

def guess_by_computer(x):
    low=1
    high=x
    character='a'
    score=10
    if score >0:
        while character != 'c' and score>0:
            ran_num=random.randint(low,high)
            print(f"Is {ran_num} the number? If NO! Press H for High,Press L for Low,Press C for Correct")
            character=input("Enter answer : ").lower()
            if(character == 'h'):
                high=ran_num-1
                score-=1
            elif(character=='l'):
                low=ran_num+1
                score-=1
    if score>0:
        print(f"Hurray I guessed {ran_num} correctly..and my score is {score}")
        
    else:
        print("Chances Exceeded !! Try Again !!")
        
    return




while True:
    choice=int(input("1.For Guessing number.\n2.For Guessing number by computer\n3.For Exit\n\n"))
    if choice ==3 :
        break
    else:
        x=int(input("Enter upper limit of the range\n"))
        if choice == 1:
            guess_by_user(x)

        elif choice == 2:
            guess_by_computer(x)
        