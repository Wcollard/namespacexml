#!/usr/bin/python3

#readling data from an XML file
import os
import os.path
import xml.etree.ElementTree as ET
#locating the file
scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, "patent.xml")
#parsing the file
tree= ET.parse(filename)
root=tree.getroot()

#identifying the namespace
namespace= {'pair': 'urn:us:gov:uspto:pair'}

#printing the serial no
for ApplicationStatusData in root.findall('pair:ApplicationStatusData', namespace):
        try:
                ApplicationNumber = ApplicationStatusData.find('pair:ApplicationNumber', namespace).text
                AttorneyDocketNumber= ApplicationStatusData.find('pair:AttorneyDocketNumber', namespace).text
                FilingDate= ApplicationStatusData.find('pair:FilingDate', namespace).text
                ApplicationStatusText= ApplicationStatusData.find('pair:ApplicationStatusText', namespace).text
                print(ApplicationNumber, AttorneyDocketNumber, FilingDate, ApplicationStatusText)
        except:
                print(ApplicationNumber, 'NONE', FilingDate, ApplicationStatusText)