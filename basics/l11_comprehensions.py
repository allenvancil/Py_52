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

# Dict conprehensions from Tuples

device = {item[0]: item[1] for item in device_info}
print("\ndevices useing dict comprehension:\n\t\t", device)
print("More nicely formated")
for key, value in device.items():
    print(f"{key:>16s} : {value}")

device_info_str = "name:r3-L-n7, vendor:cisco, model:catalyst 2960, os:ios, version:12.1(T)"

dev_info_pair = [kv_pair.split(":") for kv_pair in device_info_str.split(",")]
#split dev_info_str into series of 2 element list that could be accessed as item[0] and item[1] as a 1st, 2nd, etc. loops in for loop.
device = {item[0]: item[1] for item in dev_info_pair}
print("\ndevice:\n\n", device)
print("\nMore nicely formated\n\n")
for key, value in device.items():
    print(f"{key:>16s} : {value}")


device = {item.split(":")[0]: item.split(":")[1] for item in device_info_str.split(",")}
print("\nUsing dict conprehesion\n\t\t", device )
print("\nNicely formatted:\n\n")
for key, value in device.items():
    print(f"{key:>16s} : {value}")















