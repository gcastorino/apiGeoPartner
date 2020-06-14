from pycpfcnpj import cpfcnpj
import re


class Check:
    def _is_found(self, field, data):
        """ Check is found
            @param field : string
            @param data : object
            @return: boolean
        """
        if field in data:
            return True
        return False

    def _is_requered(self, data):
        """ Check is requered
            @param data : object
            @return: boolean
        """
        if data:
            return True
        return False

    def _is_list(self, data):
        """ Check is list
            @param data : string
            @return: boolean
        """
        if type(data) is list:
            return True
        return False

    def _is_dict(self, data):
        """ Check is dict
            @param data : string
            @return: boolean
        """
        if type(data) is dict:
            return True
        return False

    def _is_string(self, data):
        """ Check is string
            @param data : string
            @return: boolean
        """
        if type(data) is str:
            return True
        return False

    def _is_int(self, data):
        """ Check is number
            @param data : string
            @return: boolean
        """
        try:
            int(data)
            return True
        except:
            return False

    def _is_min_length(self, data, min_length):
        """ Check is min length
            @param data : string
            @param min_length : int
            @return: boolean
        """
        if len(data) >= min_length:
            return True
        return False

    def _is_length(self, data, length):
        """ Check is length
            @param data : string
            @param length : int
            @return: boolean
        """
        if len(data) == length:
            return True
        return False

    def _is_cnpj(self, data):
        """ Check is cnpj
            @param data : string
            @return: boolean
        """
        return cpfcnpj.validate(data)

    def _is_lnt(self, data):
        """ Check is lnt
            @param data : string
            @return: boolean
        """
        return re.search(
            r'^(\+|-)?((\d((\.)|\.\d{1,6})?)|(0*?\d\d((\.)|\.\d{1,6})?)|(0*?1[0-7]\d((\.)|\.\d{1,6})?)|(0*?180((\.)|\.0{1,6})?))$', str(data))

    def _is_lat(self, data):
        """ Check is lat
            @param data : string
            @return: boolean
        """
        return re.search(
            r'^(\+|-)?((\d((\.)|\.\d{1,6})?)|(0*?[0-8]\d((\.)|\.\d{1,6})?)|(0*?90((\.)|\.0{1,6})?))$', str(data))
