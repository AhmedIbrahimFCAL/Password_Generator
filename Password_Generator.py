# Author: Ahmad_Ibrahim_AbuDanckash.
import random
import string

# The Functions Definitions
# This function check the input is valid number or not
def chick_number(num):
    if num=="":
        print("Please, don't leave it empty.")
        return True
    for i in num:
        if i!="0" and i!="1" and i!="2" and i!="3" and i!="4" and i!="5" and i!="6" and i!="7" and i!="8" and i!="9":
            print("")
            return True

# The Main Program
# Welcome message for user
print("\n***************  Welcome to the Password Generator!  ***************\n\nThis program prepares a password from letters, numbers, and symbols.\n\n")

while True:
    x,num1,num2,num3=0,0,0,0
# Read the total number for Password
    x = input("Please, enter the total number of character in the password: ").strip()
    while chick_number(x):
        x = input("\nYour input os not valid.\nPlease, enter the total number of character in the password: ").strip()
    x = int(x)

    num1 = input("Please, enter the number of letters in the password: ").strip()
    while chick_number(num1):
        num1 = input("\nyour input is not valid.\nPlease, enter the number of letters in the password: ").strip()
    num1 = int(num1)

    if num1==x:
        break
    elif num1>x:
        print("Invalid Input!\nA number of the letters is greater than the number of character.\n")
        continue
    num2 = input("Please, enter the number of numbers in the password: ").strip()
    while chick_number(num2):
        num2=input("\nyour input is not valid.\nPlease, enter the number of numbers in the password: ").strip()
    num2 = int(num2)
    if num1+num2==x:
        break
    elif num1+num2>x:
        print("Invalid Input!\nthe number of letters and the number of numbers is greater than the number of character.\n")

    num3 = input("Please, enter the number of symbols in the password: ").strip()
    while chick_number(num3):
        num3 = input("\nYour input is not valid.\nPlease, enter the number of symbols in the password: ").strip()
    num3 = int(num3)
#check the input number is the total number or not
    if num1+num2+num3!=x:
        print("Invalid input.\nThe sum of letters,numbers,and symbols doesn't match the password.\n")
    else: break

thepassword=[]
#Generate the password
thepassword+=random.choices(string.ascii_letters,k=num1)
thepassword+=random.choices(string.digits,k=num2)
thepassword+=random.choices(string.punctuation,k=num3)

random.shuffle(thepassword)

print("Generated Password: ","".join(thepassword)+"\n\nThanks for using my program.")
# Thanks for reading my code