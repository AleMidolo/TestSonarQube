def _update_context(self, context):
    # Inicializar diccionario de errores si no existe
    if not hasattr(context, 'error'):
        context.error = {}

    # Mapeo de nombres de campos a coordenadas x,y,z
    coord_map = {'E': 'x', 'n': 'y', 't': 'z'}
    
    # Iterar sobre los campos del grafo
    for field in self.fields:
        # Buscar campos de error que terminen en _low o _high
        if field.endswith('_low') or field.endswith('_high'):
            # Obtener el nombre base del campo (sin _low/_high)
            base = field.rsplit('_', 1)[0]
            # Obtener el tipo de error (low/high)
            error_type = field.rsplit('_', 1)[1]
            
            # Si el campo base está en el mapeo de coordenadas
            if base in coord_map:
                coord = coord_map[base]
                # Crear subdiccionario si no existe
                if coord not in context.error:
                    context.error[coord] = {}
                    
                # Guardar el índice del campo de error
                key = f"{coord}_{error_type}"
                context.error[coord][error_type] = {"index": self.fields.index(field)}