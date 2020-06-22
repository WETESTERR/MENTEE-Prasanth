import json


with open("test.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

product = jsonObject['product']
overall = jsonObject['overall']
text = jsonObject['text']

print(product)
print(overall)
print(text)