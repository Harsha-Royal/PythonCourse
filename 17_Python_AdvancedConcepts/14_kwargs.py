def marks(**kwargs):

    # kwargs is a dictionrys all the key value pairs are passed to the marks function

    for item in kwargs.keys():
        print(f"name is {item} and marks obtained is {kwargs[item]}")


marks(shubham=50,Harsha=100,teja = 99,sree=90)