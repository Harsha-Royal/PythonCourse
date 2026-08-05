age = int(input("Please enter your age: "))


if(age > 18):
    print("You can vote.")
    print("Thank you for participating in the democratic process.")
elif(age == 18):
    print("Congratulations on reaching the voting age!")
    print("You can vote now.")
else:
    print("You are not eligible to vote yet.")
    print("Please wait until you reach the voting age.")


print("End of program.")
