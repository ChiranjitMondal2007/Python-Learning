 #* Q. Write a program to find the greatest of four numbers entered by the user.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1 > num2 and num1 > num3 and num1 > num4):
    print("Number 1 is greatest")

elif (num2 > num1 and num2 > num3 and num2 > num4):
    print("Number 2 is greatest")

elif (num3 > num1 and num3 > num2 and num3 > num4):
    print("Number 3 is greatest")

else:
    print("Number 4 is greatest")