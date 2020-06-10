from model import Mongo


class Partner:
    def __init__(self):
        """ Access Database Partner
        """
        conn = Mongo()
        self.db = conn.db()
        self.table = self.db.partner

    def find(self, id):
        """ search register
        @param id : string
        @return: result query find
        """
        return self.table.find_one({'_id': id})

    def find_geo(self, lnt, lat):
        """ search register
        @param id : string
        @return: result query find
        """
        return self.table.find({'coverageArea': {'$geoIntersects': {'$geometry': {type: "Point", 'coordinates': [lnt, lat]}}}})

    def insert(self, data):
        """ Insert data  
        @param data : object
        @return: boolean
        """
        print(self.table.insert_one(data))
        return True

    def update(self, id, data):
        """ Update data  
        @param id : string
        @param data : object
        @return: boolean
        """
        print(self.table.replace_one({'_id': id}, {"$set": data}))
        return True

    def delete(self, id):
        """ Update data  
        @param id : string
        @return: boolean
        """
        print(self.table.delete_one({'_id': id}))
        return True
