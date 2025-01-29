from l00_inventory import inventory
import json


##### this program convert python_inventory to json_inventory via "dumps(pythonFile)"
#  json is string, python is a data structure
with open("l00_inventory.json", "w") as json_out:
    json_out.write(json.dumps(inventory, indent=4))

with open ("l00_inventory.json", "r") as json_in:
    json_invent = json_in.read()

print("l00_inventory.json file:", json_invent)

##### converts json_inventory to python_inventory via "loads(jsonFile)"

saved_invent = json.loads(json_invent)
if saved_invent == inventory:
    print("worked, saved = the original")
else:
    print("failed not the same")


####   converted for python data structure to json string, then back, got same data structure

