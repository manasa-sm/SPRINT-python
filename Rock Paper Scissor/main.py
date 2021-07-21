import random
choices=['rock','paper','scissor']
comp=0;me=0;
print("Welcome to the Game of Rock, Paper and Scissors 🥔 🧻 ✂")
for i in range(1,11):
    a=input("Enter your choice (rock/paper/scissors) : ")
    c=random.choice(choices)
    print("The computer chose : ",c)
    if( (a=='rock' and c=='rock') or (a=='paper' and c=='paper') or (a=='scissors' and c=='scissors')):
        print("We think so alike (●'◡'●)")
    elif((a=='rock' and c=='scissors') or (a=='paper' and c=='rock') or (a=='scissors' and c=='paper')):
        me+=1
    else:
        comp+=1
    print("The score after %d rounds is : " %i)
    print("Me : %s" %me)
    print("Comp : %s" %comp)

if(comp>me):
    print("I beat you puny human.")
elif(me>comp):
    print("I beat you dumb computer")
else:
    print("Hehe. Its a draw.")

    
