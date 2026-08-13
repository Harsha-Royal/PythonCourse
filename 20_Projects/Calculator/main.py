try:
    a = int(input("Enter the first number: "))

    b = int(input("Enter the second number: "))

    print("what kind of operation do you want to perform. press + for addition\n press - for substraction \nPress / for divison\npress * for Multiplication")

    o = input("Enter operation: ")

    match o:
        case "+":
            print(f"The result is : {a+b}")
        case "-":
            print(f"The result is : {a-b}")
        case "/":
            print(f"The result is : {a/b}")
        case "*":
            print(f"The result is : {a*b}")
        case default:
            print(f"Enter valid operation")

except Exception as e:
    print("Enter a valid value of a and b")