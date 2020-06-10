import geojson


class Hydrator:
    def __init__(self, data):
        self.data = data

    def enconde_partner(self):
        return {
            "tradingName": self.data['tradingName'],
            "ownerName":  self.data['ownerName'],
            "document": self.data['document'],
            "coverageArea": geojson.dump(self.data['coverageArea']),
            "address": geojson.dump(self.data['address'])
        }

    def decode_partner(self):
        return {
            "tradingName": self.data['tradingName'],
            "ownerName":  self.data['ownerName'],
            "document": self.data['document'],
            "coverageArea": geojson.loads(self.data['coverageArea']),
            "address": geojson.loads(self.data['address'])
        }
