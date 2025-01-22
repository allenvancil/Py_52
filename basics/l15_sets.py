avail_ips = set()
used_ips = set()

def print_ips():
    print(f"Available ips:  {avail_ips}")
    print(f"Used ips:  {used_ips}")

print("/n/n--------------Main Program----------------------\n")

if __name__ == "__main__":
    for index in range(180, 200, 3):
        avail_ips.add("10.0.1." + str(index))

    print_ips()
    while True:
        ip_address = input("Enter IP address to allocate: \n>>")
        if not ip_address:
            print("\nExiting 'sets' application")
            exit()

        if ip_address in avail_ips:

            print(f"--allocated IP address:  {ip_address}")
            avail_ips.remove(ip_address)
            used_ips.add(ip_address)

            print_ips()

            if len(avail_ips.intersection(used_ips)) > 0:
                print("\n-- Error: one or more ip in boths sets")

            else:
                print("-- IP address not found in available IPs\n")
                