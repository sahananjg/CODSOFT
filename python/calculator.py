# calculator
import math
def add():
    a = int(input("enter the 1st no:"))
    b = int(input("enter the 2nd no:"))
    print(a+b)
def sub():
    a = int(input("enter the 1st no:"))
    b = int(input("enter the 2nd no:"))
    print(a-b)
def mul():
    a = int(input("enter the 1st no:"))
    b = int(input("enter the 2nd no:"))
    print(a*b)
def div():
    a = int(input("enter the 1st no:"))
    b = int(input("enter the 2nd no:"))
    print(a/b)
def expo():
    a = int(input("enter the 1st no(base):"))
    b = int(input("enter the 2nd no(power_):"))
    print(a**b)
def sqt():
    a = int(input("enter the number:"))
    b = math.sqrt(a)
    print(b)

print(" ******** Calculator ******** ")
print("1.Addition")
print("2.Subraction")
print("3.Multiplication")
print("4.Division")
print("5.Power of")
print("6.Root of")
print("7.Exit")
while(True):
    choice = int(input("Enter the Option"))
    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        div()
    elif choice == 5:
        expo()
    elif choice == 6:
        sqt()
    elif choice == 7:
        print("you are exit")
        break
    else:
        print("Invaild choice")
        
    
