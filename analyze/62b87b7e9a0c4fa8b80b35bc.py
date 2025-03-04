def _update_context(self, context):
    # Dictionary to map field names to x,y,z coordinates
    coord_map = {'E': 'x', 't': 'y', 'phi': 'z'}
    
    # Find error fields in the graph
    for field in self.fields:
        # Check for error fields (those ending in _low or _high)
        if field.endswith('_low') or field.endswith('_high'):
            # Get base field name without _low/_high
            base_field = field[:-4]
            # Get error direction (low/high)
            direction = field[-3:]
            
            # Map the field to x,y,z coordinate if possible
            coord = coord_map.get(base_field, base_field)
            
            # Initialize error dict if needed
            if not hasattr(context, 'error'):
                context.error = {}
                
            # Add error index to context
            if coord not in context.error:
                context.error[coord] = {}
            context.error[coord][direction] = {'index': self.fields.index(field)}
            
    return context