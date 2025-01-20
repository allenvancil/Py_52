from random import choice, randint
import string
from pprint import pprint
import time

allocated_ip_addresses = set()

# A function that creates a single random ip address

def get_rand_ip(subnet_index):
    # create random device index
    for _ in range(1, 254*4):
        device_index = randint(1, 254)
        ip = "10.0." + str(subnet_index) + "." + str(device_index)

        if ip in allocated_ip_addresses:
            continue
        allocated_ip_addresses.add(ip)
        return ip
    for device_index in range(1, 254):
        ip = "10.0." + str(subnet_index) + "." + str(device_index)

        if ip in allocated_ip_addresses:
            continue

        allocated_ip_addresses.add(ip)
    return None
# pprint(get_rand_ip(10))

# Function creates a dictionary of a random device

def create_device(device_index, subnet_index, random_ip=False):

    device = dict()

    device["name"] = (
        choice(["r2", "r3", "r4", "r6", "r10"])
        + choice(["L", "U"])
        + choice(string.ascii_letters)
    )

    # RANDOM VENDOR FROM CHOICE OF CISCO, JUNIPER, ARISTA
    device["vendor"] = choice(["cisco", "juniper", "arista"])
    if device["vendor"] == "cisco":
        device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
        if device["os"] == "ios":
            device["version"] = choice(["15", "15E", "15SY", "12.2SE"])
        elif device["os"] == "iosxe":
            device["version"] = choice(["16.9", "16.7", "16.5", "16.3"])
        elif device["os"] == "iosxr":
            device["version"] = choice(["6.2", "6.0", "5.4", "5.1"])
        elif device["os"] == "nexus":
            device["version"] = choice(["8.2", "8.0", "7.3", "7.1"])
    elif device["vendor"] == "juniper":
        device["os"] = "junos"
        device["version"] = choice(["12.3R12-S15", "15.1R7-S6", "18.4R2-S3", "15.1X53-D591"])
    elif device["vendor"] == "arista":
        device["os"] = "eos"
        device["version"] = choice(["4.24.1F", "4.23.2F", "4.22.1F", "4.21.3F"])

    if random_ip:
        device["ip"] = get_rand_ip(subnet_index)
    else:
        device["ip"] = "10.0." + str(subnet_index) + "." + str(device_index)

    return device
# pprint(create_device(5, 10))

def create_devices(num_dev=1, num_subnet=1, random_ip=False):

    created_devices = list()

    if num_dev > 254 or num_subnet > 254:
        print("error: too many subnet or devices")
        return created_devices

    print("Beginning device creation...")
    time.sleep(2)
    for subnet_index in range(1, num_subnet+1):

        for device_index in range(1, num_dev+1):

            device = create_device(device_index, subnet_index, random_ip)
            created_devices.append(device)

    print("completed device creation")

    return created_devices
# pprint(create_devices(5,1))

def create_devices_tuple(num_dev=1, num_subnet=1):

    return tuple(create_devices(num_dev=num_dev, num_subnet=num_subnet))

# pprint(create_devices_tuple(5,1))

def create_network(num_dev=1, num_subnet=1):

    devices = create_devices(num_dev, num_subnet)
    network = dict()
    network["subnets"] = dict()
    for device in devices:
        subnet_address_bytes = device["ip"].split(".")
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
# pprint(create_network(5,2))

def create_devices_gen(num_dev=1, num_subnet=1):
    if num_dev > 254 or num_subnet > 254:
        print("error: too many subnets or devices")
        return None

    for subnet_index in range(1, num_subnet+1):
        for device_index in range(1, num_dev+1):
            device = create_device(device_index, subnet_index)
            yield device

