 #* Q.> Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Enter a post :")

keyword_harry = post.count("harry")

if(keyword_harry>0):
    print("This post is talking about harry")

else:
    print("This post is not talking about harry")
  

