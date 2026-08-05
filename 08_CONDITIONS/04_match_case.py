a = int(input("enter your  number between 1 and 10: "))

match a : 
    case 1:
        print("you won a car`")
    case 2:
        print("you won a camera")
    case 3:
        print("you won a bicycle")
    case _:
        print("better luck next time")