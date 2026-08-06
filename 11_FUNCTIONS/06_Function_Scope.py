z = 8 # now z is a Global Variable


def add(a,b):
    #a and b are local variables
    c = a+b 

    z = 0 # it creates a new local variable and destroys itself after the function returns

    return c #variable c will be deleted after it returns the value

print(add(3,4))
#print(c) will get error undefined because the c 
print(z) # output: 8 



