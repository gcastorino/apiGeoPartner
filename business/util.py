from pycpfcnpj import cpfcnpj


class Util:
    def _is_found(self, field, data):
        if field in data:
            return True
        return False

    def _is_requered(self, data):
        if data:
            return True
        return False

    def _is_string(self, data):
        if type(data) is str:
            return True
        return False

    def _is_min_length(self, data, min_length):
        if len(data) >= min_length:
            return True
        return False

    def _is_length(self, data, length):
        if len(data) == length:
            return True
        return False

    def _is_cnpj(self, data):
        return cpfcnpj.validate(data)
