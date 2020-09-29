#Written by Christian Bjørk Christiansen 
import csv
import xml.etree.ElementTree as ET
from xml.dom import minidom
from random import randint
from msgPacker import MsgPacker
import requests

def main():

    writeToXML()

def writeToXML():
    msgPacker = MsgPacker()

    #Open file and read data from people.csv
    with open("../data/people.csv", "r") as data: 
        people = csv.reader(data)
        #Skips first row, which is the attribute names
        next(people, None)
        #For every person found, do the following
        for person in people:
            root = ET.Element('Person')
            child_fn = ET.SubElement(root, 'FirstName')
            child_fn.text = person[0]
            child_ln = ET.SubElement(root, 'LastName')
            child_ln.text = person[1]git 
            child_cpr = ET.SubElement(root, 'CprNumber')
            cpr_nr = "%0.10d" % randint(0, 99999999)
            child_cpr.text = cpr_nr

            print (prettify(root))

            json_object = msgPacker.addToJsonObject(person, cpr_nr)
            msgPacker.serializeJson(json_object)

            
            #TODO: Implement
            #Send post request
            # r = requests.post('http://localhost:8080/nemID', data=root)
            # print(r.status_code)

# from https://pymotw.com/2/xml/etree/ElementTree/create.html
def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

   
if __name__ == "__main__":
    main()