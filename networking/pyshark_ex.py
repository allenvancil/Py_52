import pyshark


def print_packet_summary(pkt):
    print("    ", str(pkt)[:120])


# CAPTURE EVERYTHING AND PRINT PACKET SUMMARIES
print("\n----- Packet summaries --------------------")
capture = pyshark.LiveCapture(interface='enp0s3', only_summaries=True)

print("\n----- Packet summaries --------------------")
for i, packet in enumerate(capture.sniff_continuously()):
    print_packet_summary(packet)
    if i >= 9:  # Stop after 10 packets
        break
