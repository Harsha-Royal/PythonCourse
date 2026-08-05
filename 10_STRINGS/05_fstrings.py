# String formatting using f-strings in Python

template = "Hello, {name}! Welcome to {place}."

name = "Harsha"
place = "Python Programming"

# Using f-strings for formatting
formatted_string = f"Hello, {name}! Welcome to {place}."
print(formatted_string)  # Output: Hello, Harsha! Welcome to Python Programming.    

#or 

print(f"Hello, {name}! Welcome to {place}.")  # Output: Hello, Harsha! Welcome to Python Programming.

#or

print(template.format(name=name, place=place))  # Output: Hello, Harsha! Welcome to Python Programming.

# You can also use expressions inside f-strings

#ord and chr functions are used to convert between characters and their corresponding ASCII values.

char = 'A'
ascii_value = ord(char)
print(f"The ASCII value of '{char}' is {ascii_value}.")  # Output: The ASCII value of 'A' is 65.

# Convert ASCII value back to character
ascii_value = 66
char = chr(ascii_value)
print(f"The character corresponding to ASCII value {ascii_value} is '{char}'.")  # Output: The character corresponding to ASCII value 66 is 'B'.

