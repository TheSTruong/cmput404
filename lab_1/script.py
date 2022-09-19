import requests

print(requests.__version__)

print(requests.get("http://www.google.com/"))

r = (requests.get("https://raw.githubusercontent.com/TheSTruong/cmput404/main/script.py"))

content = r.text

with open("script.py", "w") as file:
	file.write(content)

print(content)
