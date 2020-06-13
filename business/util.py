from pycpfcnpj import cpfcnpj


class Util:
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

    def _is_string(self, data):
        """ Check is string
            @param data : string
            @return: boolean
        """
        if type(data) is str:
            return True
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
