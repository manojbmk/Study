import json

a = {
    'name' : 'Manoj',
    'age' : 25,
    'marks' : [90,95,98,88],
    'pass' : True,
    'object' : {
        'colour' : ('red','blue')
    }
}

with open("demo.json","w") as fh:
    fh.write(json.dumps(a,indent=2))

print(json.dumps(a,indent=3,sort_keys=True)) #Function which converts a dictionary to json data 

with open("demo.json",'r') as fh:
    json_str = fh.read()
    json_value = json.loads(json_str) #Convets a json or str values to dictionary 
    print(json_value)