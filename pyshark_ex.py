import pyshark

def print_pak(pkt):
    print("   ", str(pkt)[:120])
          
print('\n----------Packet summeries------------\n')

capt = pyshark.LiveCapture(interface='Wi-Fi 4', only_summeraries=True)
capt.sniff(packet_count=10)

for packet in capt:
    print_pak(packet)
