from pathlib import Path

file_path = Path(__file__).parent / "Harsha.txt"

with open(file_path , "r") as f:
    content = f.read()
    print(content)
