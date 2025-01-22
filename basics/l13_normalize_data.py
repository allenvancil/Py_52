from ipaddress import IPv4Address

#-----------------String Normalization----------------------

dev_1 = {
    "name": "sbx-n9kv-ao",
    "vendor": "cisco",
    "model": "Nexus9000 C9300v Chassis",
    "os": "nxos",
    "version": "9.3(3)",
    "ip": "10.1.1.1",
    1: "any data goes in here",
}

dev_2 = {
    "name": "SBx-n9kv-AO",
    "vendor": "Cisco",
    "model": "Nexus9000 C9300v Chassis",
    "os": "NXOS",
    "version": "9.3(3)",
    "ip": "10.1.1.1",
    1: "any data goes in here",
}

#-----------using lower() to normalize data---------------
if (
    dev_1["name"].lower() == dev_2["name"].lower()
    and dev_1["vendor"].lower() == dev_2["vendor"].lower()
    and dev_1["model"].lower() == dev_2["model"].lower()
    and dev_1["os"].lower() == dev_2["os"].lower()
):
    print("data normalization lowering worked!!!")
else:
    print("What the heck Chuck!!!")

#----------using casefold() for data normalization--------------

if (
    dev_1["name"].casefold() == dev_2["name"].casefold()
    and dev_1["vendor"].casefold() == dev_2["vendor"].casefold()
    and dev_1["model"].casefold() == dev_2["model"].casefold()
    and dev_1["os"].casefold() == dev_2["os"].casefold()
):
    print("data normalization casefold worked!!!")
else:
    print("What the heck Chuck!!!")

#-----------MAC address normalization----------------

colon_mac = "a0:b1:c2:d3:e4:f5"
caps_mac = "A0:B1:C2:D3:E4:F5"
dots_mac = "a0b1.c2d3.e4f5"
hyph_mac = "A0-B1-C2-D3-E4-F5"
wacky_mac = "A0-b1.C2:D3.e4-f5"

norm_mac = "a0b1c2d3e4f5"

#This is function that remove all the cases and symbols so match norm_MAC
def normal_mac(mac):
    return mac.lower().replace(":", "").replace(".", "").replace("-", "")

if (
    normal_mac(colon_mac)
    == normal_mac(caps_mac)
    == normal_mac(dots_mac)
    == normal_mac(hyph_mac)
    == normal_mac(wacky_mac)
    == normal_mac(norm_mac)
):
    
    print("MAC address normalization seems to work!!!!")

else:
    print("Its going to be a long night...")

#----normalize IP addresses with IPv4Address class-----------

f_ip = "10.0.1.1"

#doesn't work -- IPv4Address doesn't work with leading zeros, will look at later...
s_ip = "10.000.001.001"
t_ip = "010.00.01.001"

if IPv4Address(f_ip) == IPv4Address(s_ip) == IPv4Address(t_ip):
    print("IP normalization works to!!!")
else:
    print("...a brain only a mother could love...")