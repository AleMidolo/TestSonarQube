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
            # Extraer nombre base del campo y tipo de error
            base = field.rsplit('_', 1)[0]
            error_type = field.rsplit('_', 1)[1]
            
            # Obtener índice del campo en los datos
            index = self.fields.index(field)
            
            # Determinar coordenada correspondiente
            coord = coord_map.get(base, base)
            
            # Crear estructura de error si no existe
            if coord not in context.error:
                context.error[coord] = {}
                
            # Agregar índice del error
            context.error[coord][error_type] = {"index": index}