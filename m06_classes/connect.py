from netmiko import Netmiko
import napalm
from ncclient import manager

from misc_types import DeviceType

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def connect_netmiko(hostname, username, password, port, device_type):

    print(f"\n\n-------- Connecting to {hostname} : {port}")
    netmiko_connection = Netmiko(
        hostname,
        port=port,
        username=username,
        password=password,
        device_type=device_type,
    )

    print(f"--------------- Connected!!!! -----------")

    return netmiko_connection

def disconnect_netmiko(connection):
    connection.disconnect()
    print(f"--------- Disconnected -----------")

