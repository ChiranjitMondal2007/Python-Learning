 #* Q.> Write a program to find whether a given username contains less than 10 characters or not.


username = input("Enter your username :")

no_of_characters = len(username)

print(no_of_characters)

if(no_of_characters<10):
    print("Yes, Your username contains less than 10 characters")

else:
    print("No, Your username contains greater than 10 characters")    
