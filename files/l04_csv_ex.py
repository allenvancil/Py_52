from l00_inventory import csv_inventory
import csv
from pprint import pprint
from tabulate import tabulate
import filecmp

with open("l00_invent.csv", "w") as csv_out:
    csv_write = csv.writer(csv_out)
    csv_write.writerows(csv_inventory)

with open("l00_invent.csv", "r") as csv_in:
    csv_reader = csv.reader(csv_in)
    saved_csv_invent = list()
    for device in csv_reader:
        saved_csv_invent.append(device)

print("l00_invent.csv file = \n\n", saved_csv_invent)
print("\n------------pprint csv-------------\n")
pprint(saved_csv_invent)

print("\n---------------print devices as dictionary----------\n")
devices = list()
for device_index in range(1, len(csv_inventory)):
    device = dict()
    for index, header in enumerate(csv_inventory[0]):
        device[header] = csv_inventory[device_index][index]
    devices.append(device)
print("\n-------------pprint devices as dictionary------------\n")
pprint(devices)
print("\n-----------read csv created by spreedsheet--------\n")

with open("devices_for_csv_example - Sheet1.csv", "r") as csv_in:
    csv_reader = csv.reader(csv_in)
    spreadsheet_csv_invent = list()
    for device in csv_reader:
        spreadsheet_csv_invent.append(device)
print("\nreading csv file from spreedsheet\n")
pprint(spreadsheet_csv_invent)

devices = list()
for dev_index in range(1, len(spreadsheet_csv_invent)):
    device = dict()
    for index, header in enumerate(spreadsheet_csv_invent[0]):
        device[header] = spreadsheet_csv_invent[device_index][index]
    devices.append(device)

print("\n------------output of devices from spreadsheet----------------\n")
print("\n", tabulate(devices, headers="keys"))