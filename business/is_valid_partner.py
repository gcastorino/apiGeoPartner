from business.util import Util


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
    def _tradingName(self, field='tradingName', min_length=5):
        """ Validate data tradingName
            - exist
            - Requered
            - Type string
            - Min length
        """
        if not self.util._is_found(field, self.data):
            self.errors.append({field: 'Not found'})
            return False

        if not self.util._is_requered(self.data[field]):
            self.errors.append({field: 'Required field'})
            return False

        if not self.util._is_string(self.data[field]):
            self.errors.append({field: 'Type requered str'})
        if not self.util._is_min_length(self.data[field], min_length):
            self.errors.append({field: f'Min length {min_length}'})

    # ownerName: Zé da Silva
    def _ownerName(self, field='ownerName', min_length=5):
        """ Validate data ownerName
            - exist
            - Requered
            - Type string
            - Min length
        """
        if not self.util._is_found(field, self.data):
            self.errors.append({field: 'Not found'})
            return False

        if not self.util._is_requered(self.data[field]):
            self.errors.append({field: 'Required field'})
            return False

        if not self.util._is_string(self.data[field]):
            self.errors.append({field: 'Type requered str'})
        if not self.util._is_min_length(self.data[field], min_length):
            self.errors.append({field: f'Min length {min_length}'})

    # document: 1432132123891/0001
    def _document(self, field='document', length=14):
        """ Validate data document
            - exist
            - Requered
            - Type string
            - Type min length
            - Length
            - valid Document CNPJ
        """
        if not self.util._is_found(field, self.data):
            self.errors.append({field: 'Not found'})
            return False

        if not self.util._is_requered(self.data[field]):
            self.errors.append({field: 'Required field'})
            return False

        if not self.util._is_string(self.data[field]):
            self.errors.append({field: 'Type requered str'})
        if not self.util._is_length(self.data[field], length):
            self.errors.append({field: f'Length {length}'})
        if not self.util._is_cnpj(self.data[field]):
            self.errors.append({field: f'Document invalid'})

    # coverageArea: {
    #   "type": "MultiPolygon",
    #   "coordinates": [
    #          [[[30, 20], [45, 40], [10, 40], [30, 20]]],
    #          [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]]
    #   ]
    # }

    def _coverageArea(self, field='coverageArea'):
        """ Validate data coverageArea
            - exist
            - Requered
        """
        if not self.util._is_found(field, self.data):
            self.errors.append({field: 'Not found'})
            return False

        if not self.util._is_requered(field, self.data):
            self.errors.append({field: 'Required field'})
            return False

    #    "address": {
    #      "type": "Point",
    #      "coordinates": [-46.57421, -21.785741]
    #    }

    def _address(self, field='address'):
        """ Validate data address
            - exist
            - Requered
        """
        if not self.util._is_found(field, self.data):
            self.errors.append({field: 'Not found'})
            return False

        if not self.util._is_requered(field, self.data):
            self.errors.append({field: 'Required field'})
            return False
