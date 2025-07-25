def pop_u16(self):
    """
    Remove the last two bytes of data, returning them as a big-endian
    16-bit unsigned integer.
    """
    # Get last 2 bytes
    last_two = self.data[-2:]
    
    # Remove last 2 bytes from data
    self.data = self.data[:-2]
    
    # Convert bytes to unsigned 16-bit int using big-endian byte order
    return int.from_bytes(last_two, byteorder='big', signed=False)