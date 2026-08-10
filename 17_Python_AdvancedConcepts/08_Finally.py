try:

    a = int(input("enter number 1: "))
    b = int(input("enter number 2: "))
    print(a/b)

except:
    print(f"Some error occured :")

finally:
    print("I will be executed always")