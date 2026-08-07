s = {3,32,43,56} 


print(s) # output {32, 43, 56, 3} will be random and not in the same series as we declared because set is unordered collection of data type.

print(type(s)) # output <class 'set'> because s is a set data type.

#***
#print(s[2]) #TypeError: 'set' object is not subscriptable we cannot fetch set values using index because those are not stored in particular order those are stored randomly.

print(len(s)) # output 4 because there are 4 elements in the set s.

print(3 in s) # output True because 3 is present in the set s.

print(5 in s) # output False because 5 is not present in the set s.

print(3 not in s) # output False because 3 is present in the set s.

print(5 not in s) # output True because 5 is not present in the set s.

