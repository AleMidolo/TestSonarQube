class IPAddress:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def is_valid(self):
        octets = self._get_octets()
        return len(octets) == 4 and all(self._is_valid_octet(octet) for octet in octets)

    def _get_octets(self):
        return self.ip_address.split('.')

    def _is_valid_octet(self, octet):
        return octet.isdigit() and 0 <= int(octet) <= 255

    def get_octets(self):
        return self._get_octets() if self.is_valid() else []

    def get_binary(self):
        if self.is_valid():
            return '.'.join(self._to_binary(octet) for octet in self.get_octets())
        return ''

    def _to_binary(self, octet):
        return format(int(octet), '08b')