A = {1,2,3,4,5,6}
B = {5,6,7,8,9,10}

# print(A | B) 
# print(A.union(B))  
#* A union B --> Take the elements from both Sets and then delete the duplicates



# print(A.intersection(B))
# print(A & B) 
#! Returns only common elements present in both sets.



# print(A.difference(B))
# print(A - B)
#& Returns elements present in first set but not in second set.



print(A.symmetric_difference(B))
print(A ^ B)
#^ Returns elements that are in either set but not in both.