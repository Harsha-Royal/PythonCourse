# Walras operator Combines assignment and evaluation in a single expression

def some_function():
    print("function printing 1")
    print("function printing 2")
    print("function printing 3")
    print("function printing 4")
    print("function printing 5")
    print("function printing 6")
    return 70 # did some operation and printing the values


#Now i want to print the values only if it is greater than 50 then only this operation should happen

#Below one will execute the function twice and the value we are not storing the value which executed first
# if(some_function() > 50):
#     some_function()

if( (a:=some_function()) > 50): #parantesis is required for the walras operator otherwise it will take value as boolean because of the comparision happening inside if paranthesis
    print(a)
else :
    print("Its not greater than 50")

while True:
    if(data := input("Enter the value:") != 'q'):
        print(data)
    else:
        break
