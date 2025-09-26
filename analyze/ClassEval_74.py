class Server:

    def __init__(self):
        self.white_list = []
        self.send_struct = {}
        self.receive_struct = {}

    def add_white_list(self, addr):
        if self._is_addr_in_white_list(addr):
            return False
        self.white_list.append(addr)
        return self.white_list

    def del_white_list(self, addr):
        if not self._is_addr_in_white_list(addr):
            return False
        self.white_list.remove(addr)
        return self.white_list

    def recv(self, info):
        if not self._is_info_structure_valid(info):
            return -1
        addr = info["addr"]
        content = info["content"]
        if not self._is_addr_in_white_list(addr):
            return False
        self.receive_struct = {"addr": addr, "content": content}
        return self.receive_struct["content"]

    def send(self, info):
        if not self._is_info_structure_valid(info):
            return "info structure is not correct"
        self.send_struct = {"addr": info["addr"], "content": info["content"]}

    def show(self, type):
        if type == "send":
            return self.send_struct
        elif type == "receive":
            return self.receive_struct
        return False

    def _is_addr_in_white_list(self, addr):
        return addr in self.white_list

    def _is_info_structure_valid(self, info):
        return isinstance(info, dict) and "addr" in info and "content" in info