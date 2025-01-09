dev_str = "  r3-L-n7, cisco, catalyst 2960, ios, extra stupid stuff"

# non list comprehension

device = list()
for item in dev_str.split(","):
    device.append(item.strip())
print("\ndevice using for loop:\n\t\t", device)

# List comprehension
# Start with the for loop, the go to item.strip
device = [item.strip() for item in dev_str.split(",")]
print("\nhere is device using comprehension:\n\t\t", device)

# list comprehension with conditional
# this removes the item that has "stupid" in it

device = [item.strip() for item in dev_str.split(",") if "stupid" not in item]
print("\ndevice list comprehension with conditional: \n\t\t", device)

device_info = [
    ("name", "r3-L-n7"),
    ("vendor", "cisco"),
    ("model", "catalyst 2968"),
    ("os", "ios"),
]

