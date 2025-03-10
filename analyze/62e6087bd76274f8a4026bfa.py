def pop_u16(self):
    """
    Elimina los últimos dos bytes de `self.data`, devolviéndolos como un entero sin signo de 16 bits en formato big-endian.
    """
    if len(self.data) < 2:
        raise ValueError("Not enough bytes in data to pop a 16-bit integer.")
    
    # Extraer los últimos dos bytes
    byte1, byte2 = self.data[-2], self.data[-1]
    
    # Eliminar los últimos dos bytes de self.data
    self.data = self.data[:-2]
    
    # Convertir a entero sin signo de 16 bits en formato big-endian
    return (byte1 << 8) | byte2