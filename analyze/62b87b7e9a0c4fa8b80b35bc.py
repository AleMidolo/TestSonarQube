def _update_context(self, context):
    # Inicializar diccionario de errores si no existe
    if not hasattr(context, 'error'):
        context.error = {}

    # Mapeo de nombres de campos a coordenadas x,y,z
    coord_map = {'E': 'x', 'n': 'y', 't': 'z'}
    
    # Iterar sobre los campos del grafo
    for field in self.fields:
        # Buscar campos de error que terminen en _low o _high
        if field.startswith('error_') and (field.endswith('_low') or field.endswith('_high')):
            # Extraer el nombre base del campo y el tipo de error (low/high)
            base_field = field.replace('error_', '').replace('_low', '').replace('_high', '')
            error_type = 'low' if field.endswith('_low') else 'high'
            
            # Obtener la coordenada correspondiente (x,y,z)
            coord = coord_map.get(base_field, base_field)
            
            # Crear la estructura anidada para el error
            if coord not in context.error:
                context.error[coord] = {}
                
            # Almacenar el índice del campo de error
            error_key = f"{coord}_{error_type}"
            context.error[coord][error_type] = {"index": self.fields.index(field)}