#Written by Christian Bjørk Christiansen
import msgpack

class MsgPacker():

    #Serilizes the json_object into msgpack
    @classmethod
    def serializeJson(self, json_object):
        with open("msgpackages/" + json_object["CPR"] + ".msgpack", "wb") as cpr_msgpack:
            packed = msgpack.packb(json_object)
            cpr_msgpack.write(packed)


    #TODO: add nemID
    #Adds the person information to json_object
    @classmethod
    def addToJsonObject(self, person, cpr, nemID):
        json_object = {
            'f_name': person[0],
            'l_name': person[1],
            'birth_date': person[2],
            'email': person[3],
            'country': person[4],
            'phone': person[5],
            'address': person[6],
            'CPR': cpr,
            'NemID': nemID
        }
        return json_object



