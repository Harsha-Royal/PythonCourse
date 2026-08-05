name = "Harsha"

#name[start:end:step]  # This is the general syntax for slicing in Python.

print(name[0:3])  # Output: Har (characters from index 0 to 2)
print(name[3:6])  # Output: sha (characters from index 3 to 5)
print(name[:3])   # Output: Har (characters from the start to index 2)
print(name[3:])   # Output: sha (characters from index 3 to the end)
print(name[:])    # Output: Harsha (the entire string)

print(name[2:-1])  # Output: rsh (characters from index 2 to the second last character)
# same as name[2:5] because -1 refers to the last character, so it stops before that.


print(name[::2])  # Output: Hrh (every second character) skips n-1 characters, so it returns every second character starting from index 0.
print(name[1::2]) # Output: asa (every second character starting from index 1)
print(name[::-1])  # Output: ahsraH (the string reversed)
print(name[::1])  # Output: Harsha (the entire string, step of 1) skips n-1 characters, so it returns the entire string.


