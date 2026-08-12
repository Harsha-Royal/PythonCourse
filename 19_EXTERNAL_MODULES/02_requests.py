import requests

r = requests.get("http://api.github.com/events")

print(r.text)


with open("Harsha.txt","w") as f:
    f.write(r.text)

    