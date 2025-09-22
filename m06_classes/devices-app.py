from Device import Device
from misc_types import DeviceType, TransportType
from pprint import pprint

def created_devices():
    created_devices = dict()
    created_devices['nxos-netmiko'] = Device(
        name="nxos-netmiko",
        hostname="sbx-nxos-mgmt.cisco.com",
        device_type=DeviceType.CISCO_NXOS,
        transport=TransportType.NETMIKO,
    )
    created_devices['nxos-netmiko'].set_port(8181)
    created_devices['nxos-netmiko'].set_credentials(username='admin', password="Admin1234!")

    created_devices["nxos-napalm"] = Device(
        name="nxos-napalm",
        hostname="sbx-nxos-mgmt.cisco.com",
        device_type=DeviceType.NXOS,
        transport=DeviceType.NAPALM,
    )
    created_devices['nxos-napalm'].set_port(8181)
    created_devices['nxos-napalm'].set_credentials(username='admin', password='Admin1234!')

    created_devices["nxos-ncclient"] = Device(
        name="nxos-ncclient",
        hostname="sbx-nxos-mgmt.cisco.com",
        device_type=DeviceType.NEXUS,
        transport=DeviceType.NCCLIENT,
    )
    created_devices["nxos-ncclient"].set_port(8181)
    created_devices["nxos-ncclient"].set_credentials(username="admin", password="Admin1234!")

    return created_devices

# devices = created_devices()
# for _, device in devices.items():
#
#     if not device.connect():
#         print(f"----------- Connection Fail : {device.name}")
#         continue
#
#     facts = device.get_facts()
#     print(f"----------- Facts: {device.name}")
#     pprint(facts)
#
#     device.disconnect()