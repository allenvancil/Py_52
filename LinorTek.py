import re
import os
import platform


with open('../data/linortek.txt', 'r') as file:
    
    l = file.readlines() # give a block list with \n included in each entry
    
ip_reg = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"  #reg express the get ip address


# Making a list of ips of each school
ip_list = []
for i in range(len(l)):
    ip = l[i]
    ip_addr = re.search(ip_reg, ip)
    if ip_addr:
        ip_list.append(ip_addr.group())
        
    else:
        pass


def ping_ip(ip_list):
    
    for i in ip_list:

            if platform.system().lower() == "windows":
                cmd = f"ping -n 1 {i}"
            else:
                cmd = f"ping -c 1 {i}"

            response = os.system(cmd)

            if response == 0:
                print(f"Ping to {i} sucessful.")
                
            else:
                print(f"Ping to {i} not sucessful")

ping_ip(ip_list)