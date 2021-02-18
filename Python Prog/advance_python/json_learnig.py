import json
data = '''
{
    
    "children": [
        {
            "firstName": "Alice",
            "age": 8,
            "email": "alica@mail",
            "bool": false
        },
        {
            "firstName": "Bob",
            "age": 5,
            "email": null,
            "bool": false
        }
    ]
}
'''

data2 = json.loads(data)
for child in data2["children"]:
    del child["email"]
new_data = json.dumps(data2, indent=4, sort_keys=True)
print(new_data)