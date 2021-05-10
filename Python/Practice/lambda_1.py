import json
file_path = r'E:\manoj\test.json'
with open(file_path) as fp:
    json_data=json.load(fp)
print(json_data)

for i in json_data:
 print(i['name'])
 for j in i['topping']:
     print(j['type'])