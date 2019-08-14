import pandas as pd
import xml.dom.minidom
from xml.etree import ElementTree

# content = pd.read_xml('data.xml')
# print(content)
dom = ElementTree.parse('data.xml')
root = dom.getroot()
# dom = xml.dom.minidom.parse('data.xml')
# root = dom.documentElement
node_l = root.findall('d')
for i in node_l:
    a = i.findall('el')
    for b in a:
        print(b.attrib)