import xml.etree.ElementTree as ET

tree=ET.parse('files/***.xml')
root= tree.getroot()


#declaring namespace

namespace ={
  'people': "http://people.example.com",
  'characters': "http://characters.example.com"

 }

 #finding and printing from the dom

for ns in root.findall ('poeple:actor', namespace):
  name=ns.find ('people:name', namespace)
  print(name.text)

  for char in ns.findall('characters:character', namespace):
    print(' |-->', char.text)