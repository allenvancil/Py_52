from random import choice
import string
from pprint import pprint

from pkg_resources import non_empty_lines


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

def create_network(num_dev=1, num_subnet=1):

    devices = create_devices(num_dev, num_subnet)
    network = dict()
    network["subnets"] = dict()
    for device in devices:
        subnet_address_bytes = device['ip'].split(".")
        subnet_address_bytes[3] = "0"
        subnet_address = ".".join(subnet_address_bytes)

        if subnet_address not in network["subnets"]:
            network["subnets"][subnet_address] = dict()
            network["subnets"][subnet_address]["devices"] = list()
        network["subnets"][subnet_address]["devices"].append(device)

        interfaces = list()
        for index in range(0,choice([2, 4, 8])):
            interface = {
                "name": "g/0/0/" + str(index),
                "speed": choice(["10", "100", "1000"])
            }
            interfaces.append(interface)
        device["interfaces"] = interfaces
    return network
pprint(create_network(25,2))

def create_devices_gen(num_dev=1, num_subnets=1):

    if num_dev > 254 or num_subnets >254:
        print("Error!!! Too many devices/subnets")
        return None
    print("\nbeginning device creation...\n")
    for subnet_index in range(1, num_subnets + 1):
        for device_index in range(1, num_dev + 1):
            device = create_devices(device_index, subnet_index)
            yield device