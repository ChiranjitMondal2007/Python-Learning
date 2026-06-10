s ={1, 5, 32, 54, 5, 5, 5, "Harry"}
print(s, type(s))

s.add(566)
print(s)



s.update([900,567,321])
print(s)



s.remove(567)   
print(s)
#! Ek baar mai ek hi element remove kr skta hai & agar set mai element na ha to error deta hai



s.discard(1000000) #* agar element set mai na ho to bhi error nhi deta
print(s)



print(s.pop())   #^ random element remove karta hai



# s.clear()
# print(s)  #& ---> Pure set ko clear kr dete hai



s1 = s.copy()
print(s1)      #! ---> Pure set ka copy bna deta hai


