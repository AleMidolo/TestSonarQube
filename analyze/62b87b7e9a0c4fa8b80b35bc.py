def _update_context(self, context):
    # Inicializar diccionario de errores si no existe
    if not hasattr(context, 'error'):
        context.error = {}

    # Mapeo de nombres de campos a coordenadas x,y,z
    coord_map = {'E': 'x', 'n': 'y', 't': 'z'}
    
    # Buscar campos de error en el grafo
    for field in self.fields:
        # Buscar campos que terminan en _low o _high
        if field.endswith('_low') or field.endswith('_high'):
            # Obtener el nombre base del campo (sin _low/_high)
            base = field.rsplit('_', 1)[0]
            # Obtener el tipo de límite (low/high)
            limit = field.rsplit('_', 1)[1]
            
            # Si el campo base está en el mapeo de coordenadas
            if base in coord_map:
                coord = coord_map[base]
                # Crear entrada en el diccionario de errores
                error_key = f"{coord}_{limit}"
                if error_key not in context.error:
                    context.error[error_key] = {}
                # Guardar el índice del campo en el contexto
                context.error[error_key]['index'] = self.fields.index(field)