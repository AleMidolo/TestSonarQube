def pop_u16(self):
    """
    Rimuove gli ultimi due byte da `self.data`, restituendoli come un intero senza segno a 16 bit in formato big-endian.
    """
    if len(self.data) < 2:
        raise ValueError("Not enough data to pop 16 bits.")
    
    # Rimuovi gli ultimi due byte
    last_two_bytes = self.data[-2:]
    self.data = self.data[:-2]
    
    # Converti i byte in un intero senza segno a 16 bit in formato big-endian
    return (last_two_bytes[0] << 8) | last_two_bytes[1]