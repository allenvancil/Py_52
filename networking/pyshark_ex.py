import pyshark


def print_packet_summary(pkt):
    print("    ", str(pkt)[:120])


# CAPTURE EVERYTHING AND PRINT PACKET SUMMARIES
print("\n----- Packet summaries --------------------")
capture = pyshark.LiveCapture(interface='enp0s3', only_summaries=True)
capture.sniff(packet_count=10)
for packet in capture:
    print_packet_summary(packet)