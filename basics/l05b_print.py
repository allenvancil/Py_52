from L03_Function_py import create_devices
from pprint import pprint
from operator import itemgetter
from tabulate import tabulate
from datetime import datetime
from time import sleep
from random import choice
import nmap

devices = create_devices(25)

print("\n\n Printing Devices:")
pprint(devices)

print("\n\n Loops:")
for device in devices:
    sleep(.1)
    device["last heard"] = str(datetime.now())
    print(device)

print("\n\n Tabulate:")
print(
    tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys")
)

print("\n\nloop and fstring:\n")
print("    Name       Vendor :     OS  IP address         Last Heard")
print("-----------    ------       --- -----------        ------------")
for device in devices:
    print(
        f'{device["name"]:>7}   {device["vendor"]:>10}  :  {device["os"]:>6}  {device["ip"]:<15}  {device["last heard"][:-4]}'
    )

print("\n\nsorted by 'last heard':\n")
for device in sorted(devices, key=itemgetter("last heard"), reverse=False):
    print(
        f'{device["name"]:>7}   {device["vendor"]:>10}  :  {device["os"]:>6}  {device["ip"]:<15}  {device["last heard"][:-4]}'
    )

nm = nmap.PortScanner()
while True:

    ip = input("\nInput IP address to scan:  ")
    if not ip:
        break
    print(f"\n---- beginning scan of {ip}")
    output = nm.scan(ip, "22-1024")
    print(f"--- --- command: {nm.command_line()}")
    print("------------nmap output scan----------------")
    pprint(output)