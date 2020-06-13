from business.partner import Partner
import logger_config
import ujson


class PartnerCreate:
    def __init__(self, data):
        self.logger = logger_config.get_logger()
        self.data = data
        self.register = {}
        self.error = []
        self.totalizers = {
            'all': 0,
            'concluded': 0,
            'error': 0,
            'duplicate': 0,
            'system_error': 0
        }
        pass

    def process(self):
        """Process list partners
            - submit all register Json 
        """
        try:
            self.logger.info(f'--- request {len(self.data)} partner ---')
            for pdvs in self.data:
                self.totalizers['all'] = self.totalizers['all'] + 1
                self.submit(pdvs)
        except Exception as e:
            self.error = e

    def submit(self, pdvs):
        """Submit and partner
            - start partner business in register 
            - check create
            - check errors
            - check duplicate
            - add totalizers
            - add status register 
            @param pdvs : object
        """
        try:
            business = Partner(pdvs)
            business.create()
            # return register create
            if business.register:
                self.logger.info(
                    f'create partner - success - {pdvs["document"]}')
                self.totalizers['concluded'] = self.totalizers['concluded'] + 1
                self.register[pdvs["document"]] = {
                    'code': 201,
                    'register': business.register['id']
                }
            # return error payload
            if business.error:
                self.logger.error(
                    f'create partner - error - 400 - {str(business.error)}')
                self.totalizers['error'] = self.totalizers['error'] + 1
                self.register[pdvs["document"]] = {
                    'code': 400,
                    'register': business.error
                }
            # return error duplicated
            if business.conflited:
                self.logger.error(
                    f'create partner - error - 422 - Duplicate register - {pdvs["document"]}')
                self.totalizers['duplicate'] = self.totalizers['duplicate'] + 1
                self.register[pdvs["document"]] = {
                    'code': 422,
                    'document': pdvs["document"],
                    'register': 'Duplicate register'
                }
        except Exception as e:
            # return error server
            self.totalizers['system_error'] = self.totalizers['system_error'] + 1
            self.logger.error('create partner - error - 500', e)
            self.register[pdvs["document"]] = {
                'code': 500,
                'document': pdvs["document"],
                'register': e
            }
