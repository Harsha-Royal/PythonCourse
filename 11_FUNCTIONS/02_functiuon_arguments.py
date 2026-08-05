def add(x, y):    # x,y are parameters
    return x + y


result = add(5, 3) #5,3 are arguments
print(result)  # Output: 8

# keyword arguments
def subtract(x, y):
    return x - y

print(subtract(y=5, x=10))  # Output: 5



# default arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob", "Hi"))  # Output: Hi, Bob!


