
from pathlib import Path

file_path = Path(__file__).parent / "Harsha.txt"

f = open(file_path,"r")

for line in f:
    print(line)

f.close() # if we use open then we must close it