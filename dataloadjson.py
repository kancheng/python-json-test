import json

with open("./data.json", "r") as f:
    content = json.load(f)
    print(type(content))
    print(content)

print(content["datasets"][0]["id"])
