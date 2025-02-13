def pop_u16(self):
    last_two_bytes = self.data[-2:]
    self.data = self.data[:-2]
    return int.from_bytes(last_two_bytes, byteorder='big', signed=False)