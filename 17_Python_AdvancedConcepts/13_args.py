def sum(*args):
    # args will be tuple of all the values passed to sum
    total = 0

    for value in args:
        total += value

    return total

print(sum(23,43,5,2,12))

