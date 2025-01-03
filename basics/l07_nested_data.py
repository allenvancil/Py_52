from pprint import pprint
from random import choice
import copy

from util.create_utils import create_network

device = {
    "name": "r3-L-n7",
    "vendor": "cisco",
    "model": "catalyst 29/60",
    "os": "ios",
    "interfaces": [

    ]
}

print("\n\n----------------no interfaces-------------------\n")
for key, value in device.items():
    print(f"{key:>16s} : {value}")

interfaces = list()
for index in range(0, 8):
    interface = {
        "name": "g/0/0/" + str(index),
        "speed": choice(["10", "100", "1000"])
    }
    interfaces.append(interface)
device["interfaces"] = interfaces

print("\n\n-----------with interfaces-------------------\n")
for key, value in device.items():
    if key != "interfaces":
        print(f"{key:>16s} : {value}")
    else:
        print(f"{key:>16s} :")
        for interface in interfaces:
            print(f"\t\t\t{interface}")

print()
print("---------------------using pprint---------------------")
pprint(device)

print("\n\n---------------networks with device and interface--------------------\n")
network = create_network(4,4)
pprint(network)
print("\n\n---------------------Info about network-------------------\n")
print(f" -- number of subnets:  {len(network["subnets"])}")
print(f" -- list of subnets:    {network["subnets"].keys()}")
print(f" -- list of subnets without extraneous: {', '.join(network['subnets'])}")

print("\n\n-----------------------nw and dev nicely formated---------------------------\n")
for subnet_address, subnet in network['subnets'].items():
    print(f"\n -- subnet: {subnet_address}")
    for device in subnet['devices']:
        print(f"   |-- device: {device['name']:8} {device['ip']:10} {device['vendor']:6} : {device['os']:6}")

print("\n\n------------------------Assigment vs. copy----------------------------------\n")
nw_assign = network
network["subnets"]["10.0.1.0"]["devices"][0]["name"] = "different name assigned"
print(f"  ----- network == nw_assign : {network == nw_assign}")

print("\n\n----------------------------copy---------------------")
nw_copy = copy.copy(network)
network["subnets"]["10.0.1.0"]["devices"][0]["name"] = "name_other"
print(f"  ----- network == nw_copy : {network == nw_copy}")

print("\n\n----------------------------deep copy---------------------\n")
nw_deepcopy = copy.deepcopy(network)
network["subnets"]["10.0.1.0"]["devices"][0]["name"] = "name_3rdName"
print(f"  ----- network != nw_deepcopy : {network != nw_deepcopy}")