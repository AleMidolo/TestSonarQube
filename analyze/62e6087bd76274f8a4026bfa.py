def pop_u16(self):
    """
    Rimuove gli ultimi due byte da `self.data`, restituendoli come un intero senza segno a 16 bit in formato big-endian.
    """
    if len(self.data) < 2:
        raise ValueError("Non ci sono abbastanza byte per rimuovere.")
    value = int.from_bytes(self.data[-2:], byteorder='big', signed=False)
    self.data = self.data[:-2]
    return value