import napalm
import json
import copy
from connect_orgin import cisco_sandbox_devices
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import urllib3

IOS  = "ios"
NXOS = "nxos"
NXOS_SSH = "nxos_ssh"

devices  = copy.deepcopy(cisco_sandbox_devices)

devices[NXOS_SSH] = copy.deepcopy(devices[NXOS])

for device_type, device in devices.items():
    print(f"--------connecting to device {device_type} : {device["hostname"]} -----------")
    driver = napalm.get_network_driver(device_type)
    if device_type == NXOS:
        napalm_device = driver(
            hostname=device["hostname"]
            username=device["username"]
            password=device["password"]
        )

else:
    napalm_device = driver(
        hostname=device[""]
    )