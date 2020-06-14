import geojson
import ujson
import os


class Hydrator:

    def encode_partner(self, data):
        """ Convert register dataBase by Json
            @param data : object
            @return: object
        """
        return {
            os.getenv('FIELD_ID'): data[os.getenv('FIELD_ID')],
            os.getenv('FIELD_TRADING_NAME'): data[os.getenv('FIELD_TRADING_NAME')],
            os.getenv('FIELD_OWNER_NAME'): data[os.getenv('FIELD_OWNER_NAME')],
            os.getenv('FIELD_DOCUMENT'): data[os.getenv('FIELD_DOCUMENT')],
            os.getenv('FIELD_COVERAGE_AREA'): data[os.getenv('FIELD_COVERAGE_AREA')],
            os.getenv('FIELD_ADDRESS'): data[os.getenv('FIELD_ADDRESS')]
        }

    def decode_partner(self, data):
        """ Convert register Json by dataBase
            @param data : object
            @return: object
        """
        return {
            os.getenv('FIELD_ID'): int(data[os.getenv('FIELD_ID')]),
            os.getenv('FIELD_TRADING_NAME'): data[os.getenv('FIELD_TRADING_NAME')],
            os.getenv('FIELD_OWNER_NAME'): data[os.getenv('FIELD_OWNER_NAME')],
            os.getenv('FIELD_DOCUMENT'): data[os.getenv('FIELD_DOCUMENT')],
            os.getenv('FIELD_COVERAGE_AREA'): geojson.loads(ujson.dumps(data[os.getenv('FIELD_COVERAGE_AREA')])),
            os.getenv('FIELD_ADDRESS'): geojson.loads(ujson.dumps(data[os.getenv('FIELD_ADDRESS')]))
        }
