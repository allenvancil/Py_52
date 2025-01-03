from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

def create_devices(num_dev=1, num_subnet=1):

    created_devices = list()
    if num_dev > 254 or num_subnet >254:
        print("error")
        return created_devices
    
    for subnet_index in range(1,num_subnet+1):

        for device_index in range(1, num_dev+1):
            
            device = dict()


            device["name"] = (
                choice(["r2", "r3", "r4", "r6", "r10"])
                + choice(["L", "U"])
                + choice(string.ascii_letters)
            )

            device["vendor"] = choice(["cisco", "juniper", "arista"])
            if device["vendor"] == "cisco":
                device["os"] = choice(["ios", "iosxe", "nexus"])
                device["version"] = choice(["12.1(T).04", "14.07X", "8.12(S).010", "20.45"])
            elif device["vendor"] == "juniper":
                device["os"] = "junos"
                device["version"] = choice(["J6.23.1", "8.43.12", "6.45", "6.03"])
            elif device["vendor"] == "arista":
                device["os"] = "eos"
                device["version"] = choice(["2.45", "2.55", "2.92.145", "3.01"])
            device["ip"] = "10.0." + str(subnet_index) + "." + str(device_index)
            
            created_devices.append(device)
    return created_devices

if __name__ == '__main__':

    devices = create_devices(20, 1)
    print("\n", tabulate(devices, headers="keys"))
    print(type(devices))