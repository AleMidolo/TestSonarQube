def pop_u16(self):
    if len(self.data) < 2:
        raise ValueError("Not enough bytes to pop u16")
    value = (self.data[-2] << 8) | self.data[-1]  # Combine bytes in big-endian order
    self.data = self.data[:-2]  # Remove last 2 bytes
    return value