# while True :
#     try:
#        a = int(input("enter number 1: "))
#        b = int(input("enter number 2: "))

#        print(f"a / b is {a/b}")
#     except ValueError:
#         print("Donot enter invalid data formats only integers allowed")
#     except ZeroDivisionError:
#         print("cannot divide a number by O")
#     except Exception as e:
#         print(f"Some error occured :",{e})



a = int(input("enter number 1: "))
b = int(input("enter number 2: "))


if b == 0:
    raise ValueError("please don't divide the number by 0")

print(f"The divison is {a/b}")

