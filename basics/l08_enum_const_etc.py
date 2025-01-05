from random import choice
import string
from pprint import pprint
from tabulate import tabulate
from operator import itemgetter
from enum import Enum

#constants
CISCO = "cisco"
JUNIPER = "juniper"
ARISTA = "arista"

device = dict()
devices = list()
for index in range(20):

    device["name"] = (
        choice(["r2", "r3", "r4", "r6", "r10"])
        + choice(["L", "U"])
        + choice(string.ascii_letters)
    )


    # device["vendor"] = choice(["cisco", "juniper", "arista"])
    # if device["vendor"] == "cisco":
    #     device["os"] = choice(["ios", "iosxe", "nexus"])
    #     device["version"] = choice(["12.1(T).04", "14.07X", "8.12(S).010", "20.45"])
    # elif device["vendor"] == "juniper":
    #     device["os"] = "junos"
    #     device["version"] = choice(["J6.23.1", "8.43.12", "6.45", "6.03"])
    # elif device["vendor"] == "arista":
    #     device["os"] = "eos"
    #     device["version"] = choice(["2.45", "2.55", "2.92.145", "3.01"])

    #Using constants instead of literals
    #seems to print only 1 choice 20 times?????????????????
    device["vendor"] = choice([CISCO, JUNIPER, ARISTA])
    if device["vendor"] == CISCO:
        device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
        device["version"] = choice(["12.1(T).04", "14.07X", "8.12(S).010", "20.45"])
    elif device["vendor"] == JUNIPER:
        device["os"] = "junos"
        device["version"] = choice(["J6.23.1", "8.43.12", "6.45", "6.03"])
    elif device["vendor"] == ARISTA:
        device["os"] = "eos"
        device["version"] = choice(["2.45", "2.55", "2.92.145", "3.01"])

    devices.append(device)
print("\n\n", tabulate(devices, headers="keys"))

#use of class name and class variable
class Vendor:
    CISCO = "cisco"
    JUNIPER = "juniper"
    ARISTA = "arista"

device["vendor"] = choice([Vendor.CISCO, Vendor.JUNIPER, Vendor.ARISTA])
if device["vendor"] == Vendor.CISCO:
    device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
    device["version"] = choice(["12.1(T).04", "14.07X", "8.12(S).010", "20.45"])
elif device["vendor"] == Vendor.JUNIPER:
    device["os"] = "junos"
    device["version"] = choice(["J6.23.1", "8.43.12", "6.45", "6.03"])
elif device["vendor"] == Vendor.ARISTA:
    device["os"] = "eos"
    device["version"] = choice(["2.45", "2.55", "2.92.145", "3.01"])
    pprint(device)
# def create_network(num_dev=1, num_subnet=1):
#
#     devices = create_devices(num_dev, num_subnet)
#     network = dict()
#     network["subnets"] = dict()
#     for device in devices:
#         subnet_address_bytes = device['ip'].split(".")
#         subnet_address_bytes[3] = "0"
#         subnet_address = ".".join(subnet_address_bytes)
#
#         if subnet_address not in network["subnets"]:
#             network["subnets"][subnet_address] = dict()
#             network["subnets"][subnet_address]["devices"] = list()
#         network["subnets"][subnet_address]["devices"].append(device)
#
#         interfaces = list()
#         for index in range(0,choice([2, 4, 8])):
#             interface = {
#                 "name": "g/0/0/" + str(index),
#                 "speed": choice(["10", "100", "1000"])
#             }
#             interfaces.append(interface)
#         device["interfaces"] = interfaces
#     return network
# pprint(create_network(25,2))