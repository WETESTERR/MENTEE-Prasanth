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


json_data = {
    "product":"Python book",
    "overall":"4.0",
    "text":"Nice book"
}

with open('writed_json.json', 'w') as jsonFile:
    json.dump(json_data, jsonFile)
    jsonFile.close()