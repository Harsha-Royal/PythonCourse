z = 3


def add(a,b):
   
    c = a+b 

    global z # BY using global keyword we can use the global variable inside the function and change the values
    z = 0 

    #Multiple/Execusive usage of global keyword is not recommended as it will make debugging harder in future as we are not sure where the values are changing

    return c 

print(add(3,4))

print(z) # output: 0 


# can we modify the global variable inside the function
# Yes by using global keyword
