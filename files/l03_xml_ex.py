from l00_inventory import xml_inventory
import xmltodict
from pprint import pprint

# python to xml write

with open("l00_invent.xml", "w") as xml_out:
    xml_out.write(xmltodict.unparse(xml_inventory, pretty=True))

with open("l00_invent.xml", "r") as xml_in:
    save_invent = xmltodict.parse(xml_in.read())

print("\n\n------------- xml pprint convert from python data structure to xml------------\n")

pprint(save_invent)