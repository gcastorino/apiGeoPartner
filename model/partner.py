from model import Mongo
from business.hydrator import Hydrator
from bson.objectid import ObjectId
import logger_config


class Partner:
    def __init__(self):
        """ Access Database Partner
        """
        conn = Mongo()
        self.db = conn.db()
        self.table = self.db.partner
        self.hydrator = Hydrator()

    def find(self, id):
        """ search register by id
        @param id : string
        @return: result query find
        """
        item = self.table.find_one({'id': id})
        return item

    def find_document(self, document):
        """ search register by document
        @param document : string
        @return: result query find
        """
        item = self.table.find_one({'document': document})
        return item

    def find_geo(self, lnt, lat):
        """ search register by coverageArea
        @param id : string
        @return: result query find
        """
        return self.table.find(
            {
                'coverageArea': {
                    '$geoIntersects': {
                        '$geometry': {
                            'type': "Point",
                            'coordinates': [lnt, lat]
                        }
                    }
                }
            }
        )

    def insert(self, data):
        """ Insert data  
        @param data : object
        @return: register/false
        """
        try:
            register = self.table.insert_one(data)
            if register:
                return self.table.find_one({'document': data['document']})
            return False
        except Exception as e:
            logger = logger_config.get_logger()
            logger.error(f'create partner ({str(e)})')
            return False
