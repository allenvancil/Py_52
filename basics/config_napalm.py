import napalm
import filecmp
import difflib
import sys

print("\n-------------------connecting to device, compare config----------------\n")

driver = napalm.get_network_driver("ios")
with driver(hostname="192.168.254.200",
            username="cisco",
            password="cisco") as device:
    
    
    device.load_merge_candidate(filename="")