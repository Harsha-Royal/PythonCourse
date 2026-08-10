#Decorator is a function that takes a function, it creates a new function inside its body (wrapper). then it returns that new function

def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def sayHello():
    print("Hello from Decorators inside Function")




f = decorator(sayHello)
f()


#other syntax to represent the decorator is
# 
@decorator
def sayHelloNewSyntax():
    print("Hello from Decorators with new syntax")

sayHelloNewSyntax()