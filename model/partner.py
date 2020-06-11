from model import Mongo
from business.hydrator import Hydrator
from bson.objectid import ObjectId


class Partner:
    def __init__(self):
        """ Access Database Partner
        """
        conn = Mongo()
        self.db = conn.db()
        self.table = self.db.partner
        self.hydrator = Hydrator()

    def find(self, id):
        """ search register
        @param id : string
        @return: result query find
        """
        item = self.table.find_one({'_id': ObjectId(id)})
        return item

    def find_geo(self, lnt, lat):
        """ search register
        @param id : string
        @return: result query find
        """
        itens = []
        for item in self.table.find({'coverageArea': {'$geoIntersects': {'$geometry': {type: "Point", 'coordinates': [lnt, lat]}}}}):
            itens.append(self.hydrator.encode_partner(item))
        return itens

    def insert(self, data):
        """ Insert data  
        @param data : object
        @return: boolean
        """
        if not self.table.find_one({'document': data['document']}):
            register = self.table.insert_one(data)
            if register:
                return self.table.find_one({'document': data['document']})
        return False
