from connect import netmiko_connection
import re

SHOW_IP_ROUTE = "ip route"
SHOW_ARP = "arp"
SHOW_INT_DESCRIPTION = "int description"
SHOW_INT_BRIEF = "int brief"
SHOW_VERSION = "version"

IOS = "ios"
NXOS = "nxos"
IOSXR = "iosxr"
commands = {SHOW_IP_ROUTE: {IOS: "show ip route",
                            NXOS: "show ip route",
                            IOSXR: "show ip route"},
            SHOW_ARP: {IOS: "show arp",
                       NXOS: "show ip arp",
                       IOSXR: "show arp"},
            SHOW_INT_DESCRIPTION: {IOS: "show interfaces description",
                                   NXOS: "show interface description",
                                   IOSXR: "show interfaces description"},
            SHOW_INT_BRIEF: {IOS: "show ip interface brief",
                             NXOS: "show interface brief",
                             IOSXR: "show ip interface brief"},
            SHOW_VERSION: {IOS: "show version",
                           NXOS: "show version",
                           IOSXR: "show version"}
            }
for device_type in [IOSXR]:

    connection = netmiko_connection(device_type)
    print("connection:", connection)

    print(f"\n\n-------------showing running configuration for {device_type}-----")
    output = connection.send_command("show running-config")
    print(output)

    print(f"\n\n---------showing ip route for {device_type}------------")
    output = connection.send_command(commands[SHOW_IP_ROUTE][device_type])
    print(output)

    print(f"\n\n----------showing for arp table for {device_type}----------")
    output = connection.send_command(commands[SHOW_ARP][device_type])
    print(output)

    print(f"\n\n----------showing for interface description for {device_type}----------")
    output = connection.send_command(commands[SHOW_INT_DESCRIPTION][device_type])
    print(output)

    print(f"\n\n----------showing for interface brief for {device_type}----------")
    output = connection.send_command(commands[SHOW_INT_BRIEF][device_type])
    print(output)

    connection.disconnect()

print("\n\n---------Begin cycling through show commands---------")
xr_connection = netmiko_connection(IOSXR)

if xr_connection:
    print("---------connection successful------")
else:
    exit()

nxos_version_raw = None
csr_version_raw = None
xr_version_raw = None

for commannd_type, command in commands.items():
    print(f"\n-----------command: {commannd_type}-------------")

    print(f"\n\n----------- ... for IOSXR: {command[IOSXR]}------------")
    xr_output = xr_connection.send_command(command[IOSXR])
    print("\nthis is xr_output = \n",xr_output)

    if commannd_type == SHOW_VERSION:
        xr_version_raw = xr_output
    print("\nxr_version_raw = \n", xr_version_raw)
    
xr_connection.disconnect()

if xr_version_raw:
    re_xr_version_pattern = r"Ciso IOS XR Software, Version (.*)"

    xr_version_match = re.search(re_xr_version_pattern, xr_version_raw)

    if xr_version_match:
        print(f"-----> IOSXR version parsed from output: {xr_version_match.group(1)}")
    else:
        print(f"!!!!error, no version data to parse")






