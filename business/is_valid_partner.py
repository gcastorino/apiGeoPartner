from business.util import Util
import os


class ValidPartner:
    def __init__(self, data):
        self.util = Util()
        self.data = data
        self.errors = []
        self._tradingName()
        self._ownerName()
        self._document()
        self._coverageArea()
        self._address()

    #  tradingName: Adega da Cerveja - Pinheiros
    def _tradingName(self, field=os.getenv('FIELD_TRADING_NAME'), min_length=5):
        """ Validate data tradingName:
            - exist
            - requered
            - type string
            - min length
            @return: False
        """
        if not self.util._is_found(field, self.data):
            self.errors.append({field: os.getenv('ERROR_TEXT_NOT_FOUND')})
            return False

        if not self.util._is_requered(self.data[field]):
            self.errors.append({field: os.getenv('ERROR_TEXT_REQUIRED')})
            return False

        if not self.util._is_string(self.data[field]):
            self.errors.append({field: os.getenv('ERROR_TEXT_STRING')})

        if not self.util._is_min_length(self.data[field], min_length):
            self.errors.append(
                {field: f'{os.getenv("ERROR_TEXT_MIN_LENGTH")} {min_length}'})

    # ownerName: Zé da Silva
    def _ownerName(self, field=os.getenv('FIELD_OWNER_NAME'), min_length=5):
        """ Validate data ownerName:
            - exist
            - requered
            - type string
            - min length
            @return: False
        """
        if not self.util._is_found(field, self.data):
            self.errors.append({field: os.getenv('ERROR_TEXT_NOT_FOUND')})
            return False

        if not self.util._is_requered(self.data[field]):
            self.errors.append({field: os.getenv('ERROR_TEXT_REQUIRED')})
            return False

        if not self.util._is_string(self.data[field]):
            self.errors.append({field: os.getenv('ERROR_TEXT_STRING')})

        if not self.util._is_min_length(self.data[field], min_length):
            self.errors.append(
                {field: f'{os.getenv("ERROR_TEXT_MIN_LENGTH")} {min_length}'})

    # document: 1432132123891/0001
    def _document(self, field=os.getenv('FIELD_DOCUMENT'), length=18):
        """ Validate data document:
            - exist
            - requered
            - type string
            - type min length
            - length
            - valid document CNPJ
            @return: False
        """
        if not self.util._is_found(field, self.data):
            self.errors.append({field: os.getenv('ERROR_TEXT_NOT_FOUND')})
            return False

        if not self.util._is_requered(self.data[field]):
            self.errors.append({field: os.getenv('ERROR_TEXT_REQUIRED')})
            return False

        if not self.util._is_string(self.data[field]):
            self.errors.append({field: os.getenv('ERROR_TEXT_STRING')})

        if not self.util._is_length(self.data[field], length):
            self.errors.append(
                {field: f'{os.getenv("ERROR_TEXT_LENGTH")} {length}'})

        if not self.util._is_cnpj(self.data[field]):
            self.errors.append({field: os.getenv('ERROR_TEXT_DOCUMENT')})

    # coverageArea: {
    #   "type": "MultiPolygon",
    #   "coordinates": [
    #          [[[30, 20], [45, 40], [10, 40], [30, 20]]],
    #          [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]]
    #   ]
    # }

    def _coverageArea(self, field=os.getenv('FIELD_COVERAGE_AREA')):
        """ Validate data coverageArea:
            - exist
            - requered
            @return: False
        """
        if not self.util._is_found(field, self.data):
            self.errors.append({field: os.getenv('ERROR_TEXT_NOT_FOUND')})
            return False

        if not self.util._is_requered(self.data[field]):
            self.errors.append({field: os.getenv('ERROR_TEXT_REQUIRED')})
            return False

    #    "address": {
    #      "type": "Point",
    #      "coordinates": [-46.57421, -21.785741]
    #    }

    def _address(self, field=os.getenv('FIELD_ADDRESS')):
        """ Validate data address:
            - exist
            - requered
            @return: False
        """
        if not self.util._is_found(field, self.data):
            self.errors.append({field: os.getenv('ERROR_TEXT_NOT_FOUND')})
            return False

        if not self.util._is_requered(self.data[field]):
            self.errors.append({field: os.getenv('ERROR_TEXT_REQUIRED')})
            return False
