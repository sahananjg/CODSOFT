import random
options =("R","P","S")
Round_no=int(input("Enter how many round you want to play"))
ucount = 0
ccount = 0
dcount = 0
for i in range(Round_no):
    print("  ")
    print("(R for rock, P for paper,S for sissors ) ")
    user =input("Enter your choice: ")
    computer = random.choice(options)
    print("computer choice",computer)
    if computer == "R" and user == "P":
        print("you Won")
        ucount+=1
    elif computer == "R" and user == "S":
        print("you loss")
        ccount+=1
    elif computer == "P" and user == "R":
        print("you loss")
        ccount+=1
    elif computer == "P" and user == "S":
        print("you won")
        ucount+=1
    elif computer == "S" and user == "R":
        print("you Won")
        ucount+=1
    elif computer == "S" and user == "P":
        print("you loss")
        ccount+=1
    else:
        print("It's draw")
        dcount+=1

print("   ")
print("your score is:",ucount)
print("computer score is:",ccount)
print("no.of round draw are:",dcount)
print("  ")
if ucount > ccount:
    print("you won the game")
elif ccount > ucount:
    print("you loss the game")
else:
    print("Game was draw")

print("  ")
print("you can give your feedback")
print("\n 1.For Good \n 2.For Modrate \n 3.For not Bad \n 4.For not Satisfied")
f=int(input("Rate your feedback (1to4)"))
print(" ")
print("*****Thank you for your feedback*****")      

   
   
   
    
