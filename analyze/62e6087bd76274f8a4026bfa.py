def pop_u16(self):
    """
    Rimuove gli ultimi due byte da `self.data`, restituendoli come un intero senza segno a 16 bit in formato big-endian.
    """
    if len(self.data) < 2:
        raise ValueError("Not enough data to pop a 16-bit unsigned integer.")
    
    # Estrae gli ultimi due byte
    byte1, byte2 = self.data[-2], self.data[-1]
    
    # Rimuove i due byte da self.data
    self.data = self.data[:-2]
    
    # Combina i due byte in un intero a 16 bit in formato big-endian
    return (byte1 << 8) | byte2