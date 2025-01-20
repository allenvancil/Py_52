from util.create_utils import create_devices
from pprint import pprint
from collections import namedtuple


print("----------------------Main Program----------------\n\n")
if __name__ == "__main__":

    device_list = create_devices(4, 1)
    device_tuple = tuple(device_list)

    print("\n--------------device list-------------\n")
    pprint(device_list)
    print("\n--------------device tuple-------------\n")
    pprint(device_tuple)

    print("\n----------device named tuple--------------\n")
    Device = namedtuple("Device", ["name", 'vendor', 'model', 'os', 'ip'])
    device = Device("sbx-n9kv-ao", "cisco", "Nexus9000 C9300v Chassis", "nxos", "10.0.1.10")
    print("  name:", device.name)
    print("vendor:", device.vendor)
    print(" model", device.model)
    print("    os:", device.os)
    print("    ip:", device.ip)

    print("\n---------------tuple with a for loop--------------\n")
    item = ("name", "vendor", "model", "os", "ip")
    for i in range(len(device)):
        print(f"{item[i]:>10s} : {device[i]}")

    print("\n---------------tuple with a for loop using enumerate--------------\n")
    item = ("name", "vendor", "model", "os", "ip")
    for i, device_item in enumerate(device):
        print(f"{item[i]:>10s} : {device[i]}")

    print("\n---------------pprint device tuple--------------\n")
    pprint(device)

    print("\n---------------convert devices into tuples--------------\n")
    devices = create_devices(10,2, True)
    devices_as_namedtuples = list()
    for device in devices:
        Device = namedtuple("Device", ["name", "vendor", "os", "version", "ip"])
        devices_as_namedtuples.append(Device(**device))

    print("\n---------------pprint devices named as tuples--------------\n")
    pprint(devices_as_namedtuples)

    print("\n--------pprint devices named as tuples better format--------------\n")
    print("   Name      Vendor   :  OS     IP Address")
    print("  ------    -------    -----    -----------")
    for device in devices_as_namedtuples:
        print(f"{device.name:>7}   {device.vendor:>10}  : {device.os:<6}  {device.ip:<15}")



