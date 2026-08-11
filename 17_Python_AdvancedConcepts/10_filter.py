'''
def is_Greater_than_9(n):
    if n>9:
        return True
    if n<9:
        return False
'''

a = [1,5,2,43,63,12,443,23,435,12,9]


#filterValues = list(filter(is_Greater_than_9,a)) #function syntax

filterValues = list(filter(lambda x : x> 9, a)) # lambda syntax

print(filterValues)