numbers = [1,4,5,35,65]

def square(n):
    return n * n


mappedvalues = map(square,numbers)


print(mappedvalues)

print(list(mappedvalues))