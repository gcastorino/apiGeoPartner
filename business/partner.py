from business.is_valid_partner import ValidPartner
from business.util import Check
from business.hydrator import Hydrator
from model.partner import Partner as db_partner
import os


class Partner:
    def __init__(self, data=''):
        self.hydrator = Hydrator()
        self.check = Check()
        self.db_partner = db_partner()
        self.data = data
        self.register = {}
        self.error = []
        self.conflited = False

    def geo_search(self, ltn, lat):
        """ search partner by geo location for coverageArea:
            - find register in data base
            - convert register 
            - validate error system
            @param ltn : string
            @param lat : string
        """
        if not self.check._is_lnt(ltn):
            self.error.append({'lnt': os.getenv('ERROR_TEXT_INCORRECT')})
            return False

        if not self.check._is_lat(lat):
            self.error.append({'lat': os.getenv('ERROR_TEXT_INCORRECT')})
            return False

        response = self.db_partner.find_geo(float(ltn), float(lat))
        if response:
            register = []
            for item in response:
                register.append(self.hydrator.encode_partner(item))
            self.register = register
        else:
            self.conflited = True
        pass

    def search(self):
        """ search partner by id:
            - find register in data base
            - convert register 
            - validate error system
        """
        if not self.check._is_int(self.data):
            self.error.append({'id': os.getenv('ERROR_TEXT_NUMBER')})
            return False
        response = self.db_partner.find(int(self.data))
        if response:
            self.register = self.hydrator.encode_partner(response)
        else:
            self.conflited = True
        pass

    def create(self):
        """ Create partner:
            - validate data
            - convert register 
            - validate document register
            - register data base
            - convert register 
            - validate error system
            @return False
        """
        validate = ValidPartner(self.data)
        if validate.errors:
            self.error = validate.errors
            return False

        register = self.hydrator.decode_partner(self.data)

        if self.db_partner.find_document(register['document']):
            self.conflited = True
            return False

        response = self.db_partner.insert(register)
        if response:
            self.register = self.hydrator.encode_partner(response)
        else:
            self.error.append({'GEO': os.getenv('ERROR_TEXT_GEO')})
        pass
