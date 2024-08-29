# Password Generator
import random
l = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G ' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' ,'X ', 'Y' , 'Z']
n = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
s = ['!' , '@' , '#' , '$' , '%' , '&' , '*' , '(' , ')' , '+']
no_l = int(input("Enter the no.of letters you want:"))
no_n = int(input("Enter the no.of numbers you want:"))
no_s = int(input("Enter the no.of symbols you want:"))
password_list = []
for i in range(1,no_l+1):
    password_list += random.choice(l)
for i in range(1,no_n+1):
    password_list += random.choice(n)
for i in range(1,no_s+1):
    password_list += random.choice(s)
c=input("Do you want the password to be easy or hard(easy/hard):")
if c == "easy":
    password = " "
    for i in password_list:
        password += i
    print(password)
else:
    random.shuffle(password_list)
    password = " "
    for i in password_list:
        password += i
    print(password)
print("exit")    
        