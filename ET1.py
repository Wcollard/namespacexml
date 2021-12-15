import xml.etree.ElementTree as ET

#tree=ET.parse("C:/Users/wcoll/OneDrive - Collard & Roe PC/Desktop/project1/actors.xml")
tree=ET.parse('actors.xml')

root= tree.getroot()


#declaring namespace

namespace ={
  'people': "http://people.example.com",
  'characters': "http://characters.example.com"

 }

 #finding and printing from the dom

for ns in root.findall ('people:actor', namespace):
  name=ns.find ('people:name', namespace)
  print(name.text)

  for char in ns.findall('characters:character', namespace):
    print(' |-->', char.text)
