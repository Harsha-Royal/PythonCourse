import os
#os is a light weight library and it was prefered to use it has limited control

a = os.listdir("dir")
print(a)
print(os.getcwd())#get current working directory

print(os.path.exists("harsha.txt"))

os.remove("sample.txt")

os.remove("dir") # It will not able to delete the directory if it was not empty 