def _update_context(self, context):
    # Dictionary to map field names to x,y,z coordinates
    coord_map = {'E': 'x', 't': 'y', 'phi': 'z'}
    
    # Find error fields in the graph data
    for field in self.fields:
        # Look for error fields that end in _low or _high
        if field.endswith('_low') or field.endswith('_high'):
            # Get base field name without _low/_high
            base_field = field[:-4]
            # Get error direction (_low or _high)
            direction = field[-4:]
            
            # Map the base field to x,y,z coordinate if possible
            coord = coord_map.get(base_field, base_field)
            
            # Initialize error dict if needed
            if 'error' not in context:
                context['error'] = {}
                
            # Add error index to context
            if coord not in context['error']:
                context['error'][coord + direction] = {}
            context['error'][coord + direction]['index'] = self.fields.index(field)
            
    return context