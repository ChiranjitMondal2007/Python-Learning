 #* Q. Write a program to accept marks of 6 students and display them in a sorted manner.

marks =[]

student1 =float(input("Enter marks of student1 :"))
marks.append(student1)

student2 =float(input("Enter marks of student2 :"))
marks.append(student2)

student3 =float(input("Enter marks of student3 :"))
marks.append(student3)

student4 =float(input("Enter marks of student4 :"))
marks.append(student4)

student5 =float(input("Enter marks of student5 :"))
marks.append(student5)

student6 =float(input("Enter marks of student6 :"))
marks.append(student6)

marks.sort()

print(marks)
