import json

newUser = {'name' : 'Lee', 'birth' : '0319',
'age' : 18}
filePath = './jsonStudy.json'
with open(filePath, 'r' , encoding='utf-8') as f:
    jsonData = json.load(f)

jsonData['users'].append(newUser)
print(jsonData)

with open(filePath, 'w', encoding='utf-8') as f:
    json.dump(jsonData, f)