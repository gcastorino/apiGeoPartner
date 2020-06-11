import geojson
import ujson


class Hydrator:

    def encode_partner(self, data):
        return {
            "id": str(data['_id']),
            "tradingName": data['tradingName'],
            "ownerName":  data['ownerName'],
            "document": data['document'],
            "coverageArea": data['coverageArea'],
            "address": data['address']
        }

    def decode_partner(self, data):
        return {
            "tradingName": data['tradingName'],
            "ownerName":  data['ownerName'],
            "document": data['document'],
            "coverageArea": geojson.loads(ujson.dumps(data['coverageArea'])),
            "address": geojson.loads(ujson.dumps(data['address']))
        }
