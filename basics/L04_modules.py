from tabulate import tabulate
from util.create_utils import create_devices

if __name__ == "__main__":
    devices = create_devices(5,2)
    print("\n", tabulate(devices, headers="keys"))