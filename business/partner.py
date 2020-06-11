from business.is_valid_partner import ValidPartner
from business.hydrator import Hydrator
from model.partner import Partner as db_partner


class Partner:
    def __init__(self, data):
        self.hydrator = Hydrator()
        self.db_partner = db_partner()
        self.data = data
        self.register = {}
        self.error = []
        self.conflited = False

    def geo_search(self, ltn, lat):
        pass

    def search(self):
        response = self.db_partner.find(self.data)
        if response:
            self.register = self.hydrator.encode_partner(response)
        else:
            self.conflited = True
        pass

    def create(self):
        validate = ValidPartner(self.data)
        if validate.errors:
            self.error = validate.errors
            return False
        register = self.hydrator.decode_partner(self.data)
        response = self.db_partner.insert(register)
        if response:
            self.register = self.hydrator.encode_partner(response)
        else:
            self.conflited = True
        pass
