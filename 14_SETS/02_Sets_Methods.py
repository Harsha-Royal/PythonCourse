s = {34,21,45,22,1}

s.add(43)
print(s)

s.remove(1)
print(s)

s.add(43)
print(s)

#s.remove(430)   #KeyError: 430, remove method will return error if not found

s.discard(430)

s.discard(10) # No error if element not found
s.pop() # Removes random elemen