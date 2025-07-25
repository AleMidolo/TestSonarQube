def pop_u16(self):
    """
    Elimina los últimos dos bytes de `self.data`, devolviéndolos como un entero sin signo de 16 bits en formato big-endian.
    """
    if len(self.data) < 2:
        raise ValueError("No hay suficientes bytes en `self.data` para extraer un entero de 16 bits.")
    
    # Extraer los últimos dos bytes
    value = self.data[-2:]
    # Eliminar los últimos dos bytes de `self.data`
    self.data = self.data[:-2]
    # Convertir a entero en formato big-endian
    return int.from_bytes(value, byteorder='big')