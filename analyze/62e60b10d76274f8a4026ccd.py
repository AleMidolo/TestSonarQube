def data(self, *keys):
    # Si no se proporcionan claves, devolver todos los datos
    if not keys:
        return dict(zip(self._fields, self))
    
    # Crear diccionario con las claves solicitadas
    result = {}
    
    for key in keys:
        # Si la clave es un índice numérico
        if isinstance(key, int):
            # Verificar que el índice esté dentro de los límites
            if key < 0 or key >= len(self):
                raise IndexError(f"Index {key} out of range")
            result[self._fields[key]] = self[key]
            
        # Si la clave es un string
        else:
            # Si la clave existe en los campos, obtener su valor
            if key in self._fields:
                idx = self._fields.index(key)
                result[key] = self[idx]
            # Si no existe, asignar None
            else:
                result[key] = None
                
    return result