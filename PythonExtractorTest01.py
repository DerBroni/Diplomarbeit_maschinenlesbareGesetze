import xml.etree.ElementTree as ET
tree = ET.parse('GVIDVDV_regelungstext.xml')
root = tree.getroot()

root.tag
'akomaNtoso'
root.attrib
{}

for child in root:
    print(child.tag, child.attrib)
