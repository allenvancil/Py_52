from util.create_utils import create_devices
from tabulate import tabulate
import time

#purpose: Calculate if list or dictionary are faster to locate device
#---------------Main program-----------------------

if __name__ == "__main__":
    devices = create_devices(num_dev=254, num_subnet=254)

    #create dicts pointing at same devices
    dev_dict = dict()
    for device in devices:
        dev_dict[device["ip"]] = device

    print("tabular output of devices ...")
    print("\n",  tabulate(devices, headers="keys"))

    while True:

        find_ip = input("Enter ip address looking for: \n >> ")
        if not find_ip:
            break

        start = time.time()
        for device in devices:
            if device["ip"] == find_ip:
                print(f"-----> found it (list): {device}")
                list_search_time = (time.time() - start) * 1000
                print(f"------ ------> in: {list_search_time} msec")
                print(f"------ ------> id of device {id(device)}")
                break
            else:
                print("IP address not found")
                continue

        start = time.time()
        if find_ip in dev_dict:
            print(f"----> found it (dict) : {dev_dict[find_ip]}")
            dict_search_time = (time.time() - start)*1000
            print(f"---- -----> in: {dict_search_time} msec") 
            print(f"------ ------> id of device: {id(dev_dict[find_ip])}")
        
        print("list search time: ", list_search_time)
        print("dictionary search time: ", dict_search_time)
        #print(f"the dictionary search was {int(list_search_time/dict_search_time)} tims as fast as the list search")

