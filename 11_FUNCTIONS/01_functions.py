a = 4
b = 6
c = 8


# average = (a + b + c) / 3
# print("The average of", a, b, c, "is:", average)  # Output: The average of 4 6 8 is: 6.0


def calculate_average(x, y, z):
    return (x + y + z) / 3.0


result = calculate_average(a, b, c)

print("The average of", a, b, c, "is:", result)  # Output: The average of 4 6 8 is: 6.0

result2 = calculate_average(10, 20, 30)
print("The average of 10, 20, 30 is:", result2)

