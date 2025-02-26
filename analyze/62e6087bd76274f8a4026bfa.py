def pop_u16(self):
    """
    Remove the last two bytes of data, returning them as a big-endian
    16-bit unsigned integer.
    """
    if len(self.data) < 2:
        raise ValueError("Not enough data to pop 16 bits.")
    
    # Pop the last two bytes
    last_two_bytes = self.data[-2:]
    self.data = self.data[:-2]
    
    # Convert to big-endian unsigned integer
    return (last_two_bytes[0] << 8) | last_two_bytes[1]