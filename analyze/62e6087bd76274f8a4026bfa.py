def pop_u16(self):
    if len(self.data) < 2:
        raise ValueError("Not enough bytes to pop u16")
    value = int.from_bytes(self.data[-2:], byteorder='big', signed=False)
    self.data = self.data[:-2]
    return value