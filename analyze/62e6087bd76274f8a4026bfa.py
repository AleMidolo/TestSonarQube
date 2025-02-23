def pop_u16(self):
    """
    Elimina los últimos dos bytes de `self.data`, devolviéndolos como un entero sin signo de 16 bits en formato big-endian.
    """
    if len(self.data) < 2:
        raise ValueError("Not enough data to pop 16 bits.")
    
    # Get the last two bytes
    last_two_bytes = self.data[-2:]
    
    # Remove the last two bytes from self.data
    self.data = self.data[:-2]
    
    # Convert the bytes to an unsigned 16-bit integer in big-endian format
    return int.from_bytes(last_two_bytes, byteorder='big', signed=False)