def pop_u16(self):
    """
    Elimina los últimos dos bytes de `self.data`, devolviéndolos como un entero sin signo de 16 bits en formato big-endian.
    """
    if len(self.data) < 2:
        raise ValueError("Not enough data to pop 16 bits.")
    
    # Extraer los últimos dos bytes
    last_two_bytes = self.data[-2:]
    # Eliminar los últimos dos bytes de self.data
    self.data = self.data[:-2]
    # Convertir los bytes a un entero sin signo de 16 bits en formato big-endian
    return int.from_bytes(last_two_bytes, byteorder='big', signed=False)