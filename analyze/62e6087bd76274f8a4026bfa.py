def pop_u16(self):
    """
    Remove the last two bytes of data, returning them as a big-endian
    16-bit unsigned integer.
    """
    if len(self.data) < 2:
        raise ValueError("Not enough data to pop a 16-bit unsigned integer.")
    byte1 = self.data.pop()
    byte2 = self.data.pop()
    return (byte2 << 8) | byte1