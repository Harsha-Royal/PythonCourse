def repeatingFunction(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):    
                func(a)
        return wrapper
    return decorator

@repeatingFunction(7)
def say_Hello(a):
    print(f"Hello {a} from say_Hello Function")

say_Hello("Harsha")


'''
    It replaces the function say_hello with this:
    def decorator(func):
    def wrapper(a):
    for i in range(n):
    say_hello(a)
    return wrapper
'''