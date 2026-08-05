
a = input("Enter First number: ")

a = int(a)  # Convert the input to an integer

print(a + 3)  # This will raise an error because input() returns a string, and you cannot add a string and an integer directly.

a = int(input("Enter First number: "))

b = int(input("Enter Second number: "))

print(a + b)
