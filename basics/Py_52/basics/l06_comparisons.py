from util.create_utils import create_devices
from pprint import pprint
from random import randint, uniform, choice
from datetime import datetime
from time import sleep

devices = create_devices(25,2)


for device in devices:
    sleep(choice([.1, .02, .05]))
    device["last heard"] = str(datetime.now())
    #print(device)

print("\n\nloop and fstring:\n")
print("    Name       Vendor :     OS  IP address         Last Heard")
print("-----------    ------       --- -----------        ------------")
for device in devices:
    print(
        f'{device["name"]:>7}   {device["vendor"]:>10}  :  {device["os"]:>6}  {device["ip"]:<15}  {device["last heard"][:-4]}'
    )

print("\n\nMaking if statments more robust:\n")
for device in devices:
    if device["vendor"].lower() != "cisco".lower():
        print(
            f'{device["name"]:>7}   {device["vendor"]:>10}  :  {device["os"]:>6}  {device["ip"]:<15}  {device["last heard"][:-4]}'
        )
print("\n\n-----------------------------comparisons----------------------------")
for index, device_a in enumerate(devices):
    for device_b in devices[index+1:]:
        if device_a['name'] == device_b['name']:
            print(f"\nFound Match!!! {device_a['name']}, ip = {device_a['ip']} matches {device_b['name']}, ip = {device_b['ip']}")
print("\n\n------------------comparison complete-------------------------\n")
print('\n\n---------------standard versions----------------------------\n')
standard_versions = dict()
for device in devices:
    vendor_os = device["vendor"] + " : " + device["os"]
    if vendor_os not in standard_versions:
        standard_versions[vendor_os] = device["version"]
pprint(standard_versions)

#_________________Doesn't work______________________________________________
"""
print("\n\n------------------List of non-compliant------------------\n")
non_compliant = dict()
for vendor_os, _ in standard_versions.items():
    non_compliant[vendor_os] = []

for device in devices:
    vendor_os = device["vendor"] + ":" + device["os"]
    print(type(vendor_os))

    if device["version"] != standard_versions[vendor_os]:
        non_compliant[vendor_os].append(device["ip"] + " version: " + device["version"])
pprint(non_compliant)
"""

print("\n\n--------------------Assign, copy, deep copy-------------------")

dev2 = devices
devices[0]["name"] = ("Device_name_1")
if dev2 == devices:
    print("Dev2 still equals devices!!!")
    print("the moral of the story is assignment is not the same a copy")
else:
    print("not what I was expecting...")
print("\n\n-------------------------Deep Copy------------------------\n")
from copy import copy, deepcopy
dev2 = deepcopy(devices)
dev2[0]["name"] = "Device_name2"
if dev2 == devices:
    print("?")
else:
    print("dev2 not longer equals devices because of deep copy")

new_devices = create_devices(25,2)
if new_devices == devices:
    print("not expected")
else:
    print('you can compare any two data sets')

print("\n\n-------------------compare SLAs---------------------\n")
SLA_avail = 96
SLA_response_t = 1.0

devices = create_devices(25,2)
for device in devices:
    device["availability"] = randint(94,100)
    device["response_time"] = uniform(0.5,1.1)

    if device["availability"] < SLA_avail:
        print(f"{datetime.now()}: {device['name']:6} - Availability {device['availability']} < {SLA_avail}")
    if device["response_time"] > SLA_response_t:
        print(f"{datetime.now()}: {device['name']:6} - Response time {device['response_time']:.3f} >{SLA_response_t}")

print("\n\n---------------------comparing classes----------------------\n")

class DeviceWithEq:
    def __init__(self, name, ip):
        self.name = name
        self.ip_address = ip

    def __eq__(self, other):
        if not isinstance(other, DeviceWithEq)
            return False
        return self.name == other.name and self.ip_address == other.ip_address
d1 = DeviceWithEq("device 1", "10.10.10.1")
d1_equal = DeviceWithEq("device 1", "10.10.10.1")
d1_different = DeviceWithEq("device 2", "10.10.1")