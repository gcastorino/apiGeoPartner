import geojson
import ujson


class Hydrator:

    def encode_partner(self, data):
        """ Convert register dataBase by Json
            @param data : object
            @return: object
        """
        return {
            "id": str(data['_id']),
            "tradingName": data['tradingName'],
            "ownerName":  data['ownerName'],
            "document": data['document'],
            "coverageArea": geojson.dumps(data['coverageArea']),
            "address": data['address']
        }

    def decode_partner(self, data):
        """ Convert register Json by dataBase
            @param data : object
            @return: object
        """
        return {
            "tradingName": data['tradingName'],
            "ownerName":  data['ownerName'],
            "document": data['document'],
            "coverageArea": geojson.loads(ujson.dumps(data['coverageArea'])),
            "address": geojson.loads(ujson.dumps(data['address']))
        }
