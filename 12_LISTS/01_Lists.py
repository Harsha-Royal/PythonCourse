#Lists are mutable it means new values can be added and old values can be update with new ones

#Lists can be collection of different datatypes


marks = [23,34,45,47,67]
mixed = [49,"Harsha",False,23.00]


print(marks[2])
print(mixed[2])

#slicing
print(marks[2:4])

#print(mixed[4]) error index out of bounds

my_list =[1,2,3]
my_list.append(4) # [1, 2, 3, 4]
my_list.insert(1,99) # [1, 99, 2, 3, 4]
my_list.remove(2) # [1, 99, 3, 4]
my_list.pop() # Removes last element -> [1, 99, 3]
my_list.reverse() # [3, 99, 1]
my_list.sort() # [1, 3, 99]


squared =[x**2 for x in range(5)]
print(squared) # Output: [0, 1, 4, 9, 16]