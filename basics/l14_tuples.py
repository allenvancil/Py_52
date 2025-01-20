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