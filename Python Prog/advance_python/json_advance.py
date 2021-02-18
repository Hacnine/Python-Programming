import json

# file = open("states.json")
# data = json.load(file) or follow the method


with open("../states.json") as file:
    data = json.load(file)

for name in data['states']:
    del name["area_codes"]

with open('../new_state.json', 'w') as f:
    json.dump(data, f, indent=4)
