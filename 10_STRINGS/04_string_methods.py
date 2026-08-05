name = "hello world! " # strings are immutable in Python, meaning you cannot change their content after they are created.

#you cannot change a string in Python because strings are immutable. If you try to change a character in a string, you will get an error.
#name[0] = "H"  # This will raise an error because strings cannot be modified in place.


a = len(name)  # This will return the length of the string, which is 12 in this case.
print(a)  # Output: 12
print(name.upper())  # Output: HELLO WORLD! (converts the string to uppercase)
print(name.lower())  # Output: hello world! (converts the string to lowercase)
print(name.title())  # Output: Hello World! (converts the first character of each word to uppercase)
print(name.capitalize())  # Output: Hello world! (converts the first character of the string to uppercase and the rest to lowercase)

print(name.strip())  # Output: hello world! (removes any leading and trailing whitespace)
print(name.lstrip())  # Output: hello world! (removes any leading whitespace)
print(name.rstrip())  # Output: hello world! (removes any trailing whitespace)

print(name.replace("world", "Python"))  # Output: hello Python! (replaces the substring "world" with "Python")
print(name.split())  # Output: ['hello', 'world!'] (splits the string into a list of words based on whitespace)
print(name.split("o"))  # Output: ['hell', ' w', 'rld! '] (splits the string into a list of substrings based on the character "o")


text = "python is fun"

print(text.startswith("python"))  # Output: True (checks if the string starts with "python")
print(text.endswith("fun"))  # Output: True (checks if the string ends with "fun")
print(text.find("is"))  # Output: 7 (returns the index of the first occurrence of the substring "is")
print(text.rfind("is"))  # Output: 7 (returns the index of the last occurrence of the substring "is")
print(text.index("is"))  # Output: 7 (returns the index of the first occurrence of the substring "is"; raises an error if not found)

print(text.find("in")) # Output: -1 (returns -1 if the substring "in" is not found)
#print(text.index("in"))  # Output: ValueError: substring not found (raises an error if the substring "in" is not found)
print(text.replace("fun", "awesome"))  # Output: python is awesome (replaces the substring "fun" with "awesome")

print(text.count("n"))  # Output: 2 (returns the number of occurrences of the substring "n")
print(text.isalpha())  # Output: False (checks if all characters in the string are alphabetic; spaces are not considered alphabetic)
print(text.isdigit())  # Output: False (checks if all characters in the string are digits)
print(text.isalnum())  # Output: False (checks if all characters in the string are alphanumeric)
print(text.isspace())  # Output: False (checks if all characters in the string are whitespace)
print(text.islower())  # Output: True (checks if all characters in the string are lowercase)
print(text.isupper())  # Output: False (checks if all characters in the string are uppercase)
print(text.isprintable())  # Output: True (checks if all characters in the string are printable)
print(text.isidentifier())  # Output: False (checks if the string is a valid identifier in Python)
print(text.isnumeric())  # Output: False (checks if all characters in the string are numeric)
print(text.isdecimal())  # Output: False (checks if all characters in the string are decimal characters)



text2 = "banana, apple, orange, mango"

print(text2.split(", "))  # Output: ['banana', 'apple', 'orange', 'mango'] (splits the string into a list of substrings based on the delimiter ", ")

print(", ".join(['banana', 'apple', 'orange', 'mango']))  # Output: banana, apple, orange, mango (joins the list of strings with the delimiter ", ")


