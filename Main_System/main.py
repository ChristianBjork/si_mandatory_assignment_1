#Written by Christian Bjørk Christiansen 
import csv
import xml.etree.ElementTree as ET
from xml.dom import minidom
from random import randint
from dataHandler import DataHandler
import requests
import json

def main():
    dataHandler = DataHandler()

    #Open file and read data from people.csv
    with open("people.csv", "r") as data: 
        people = csv.reader(data)
        #Skips first row, which is the attribute names
        next(people, None)
        #For every person found --> Create XML-body and post it
        for person in people:
            # root = ET.Element('Person')
            # child_fn = ET.SubElement(root, 'FirstName')
            # child_fn.text = person[1]
            # child_ln = ET.SubElement(root, 'LastName')
            # child_ln.text = person[2]
            # child_cpr = ET.SubElement(root, 'cprnumber')
            # cpr_nr = "%0.10d" % randint(0, 99999999)
            # child_cpr.text = cpr_nr
            # child_email = ET.SubElement(root, 'email')
            # child_email.text = person[3]

            # print (prettify(root))
            
            # #Send post request
            # response = requests.post('http://localhost:8080/nemID', data=ET.tostring(root), headers={"Content-Type": "text/xml"})
            
            # #Recive response
            # json_data = json.loads(response.text)

            # #Create json object from response data and serialize it to msgpack file
            # json_object = dataHandler.addToJsonObject(person, cpr_nr, json_data["nemID"])
            # dataHandler.serializeJson(json_object)

            userId = person[0]
            print(userId)
            url = 'http://localhost:5001/skat/pay-taxes'
            userObj = {'userId': userId}

            response = requests.post(url, json=userObj)

            print(response.text)





# Return a pretty-printed XML string for the Element.
def prettify(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

   
if __name__ == "__main__":
    main()