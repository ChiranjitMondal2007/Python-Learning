student = {"name": "Rahul", "age": 20}
print(student.keys())  #* Keys() Method 



student = {"name": "Rahul", "age": 20}
print(student.values())   #! value() method


student = {"name": "Rahul", "age": 20}
print(student.items())   #^ item() method



student = {"name": "Rahul"}
print(student.get("name"))
print(student.get("age"))    #& get() method 



student = {"name": "Rahul"}             
student.update({"age": 20})
print(student)               
#^ update method --> Dictionary ko update karta    hai ya nayi key add karta hai



student = {"name": "Rahul", "age": 20}
removed = student.pop("age")
print(removed)
print(student)
#* Specified key delete karta hai aur uski value return karta hai.