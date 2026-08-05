import math
import mymodule

import requests  # pip install requests

print(math.sqrt(16))  # Output: 4.0


#two types of modules in python
# Built-in modules: These are the modules that come pre-installed with Python. Examples include math, random, os, sys, etc.
# external modules: These are the modules that are not included with Python and need to be installed separately. Examples include NumPy, Pandas, Requests, etc.



# list of built-in modules in python : https://docs.python.org/3/py-modindex.html


mymodule.Hello()  # Output: Hello, World!



r = requests.get('https://www.google.com')
print(r.status_code)  # Output: 200 (if the request was successful) 
print(r.text)  # Output: The HTML content of the Google homepage