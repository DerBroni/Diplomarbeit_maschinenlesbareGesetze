import xml.etree.ElementTree as ET
tree = ET.parse('GVIDVDV_regelungstext.xml')
root = tree.getroot()

parser = ET.XMLPullParser(['start', 'end'])
parser.feed('<mytag>sometext')
list(parser.read_events())

parser.feed(' more text</mytag>')
for event, elem in parser.read_events():
    print(event)
    print(elem.tag, 'text=', elem.text)


for bill in root.iter('bill'):
    print(bill.attrib)