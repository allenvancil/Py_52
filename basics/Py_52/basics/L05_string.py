from pprint import pprint

dev1_str = "  r3-L-n7, cisco, catalyst 2960, ios  "

print("split:")
dev1 = dev1_str.split(",")
print(dev1)

print("remove blanks:")
dev1 = dev1_str.replace(" ","").strip(",")
print(dev1)

print("replace comma with colon:")
dev1_colon = dev1.replace(",",":")
print(dev1_colon)

dev1 = list()
for item in dev1_str.split(","):
    dev1.append(item.strip())
print("for loop and strip each item")
print("    ", dev1)

print("using comprehesion:")
dev1 = [item.strip() for item in dev1_str.split(",")]
print("    ", dev1)