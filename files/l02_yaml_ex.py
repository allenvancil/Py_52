from l00_inventory import inventory
import yaml

with open("l00_yaml_invent.yaml", "w") as yaml_out:
    yaml_out.write(yaml.dump(inventory))

with open("l00_yaml_invent.yaml", "r") as yaml_in:
    yaml_inventory = yaml_in.read()

print(yaml_inventory)

saved_invent = yaml.safe_load(yaml_inventory)

if saved_invent == inventory:
    print("yaml in the same as python")
else:
    print("these do not match")