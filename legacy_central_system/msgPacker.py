#Written by Christian Bjørk Christiansen
import msgpack

class MsgPacker():

    @classmethod
    def serializeJson(self, json_object):
        with open("../data/msgpackages/" + json_object["CPR"] + ".msgpack", "wb") as cpr_msgpack:
            packed = msgpack.packb(json_object)
            cpr_msgpack.write(packed)


    #TODO: add nemID
    @classmethod
    def addToJsonObject(self, person, cpr):
        json_object = {
            'f_name': person[0],
            'l_name': person[1],
            'birth_date': person[2],
            'email': person[3],
            'country': person[4],
            'phone': person[5],
            'address': person[6],
            'CPR': cpr
        }
        return json_object



