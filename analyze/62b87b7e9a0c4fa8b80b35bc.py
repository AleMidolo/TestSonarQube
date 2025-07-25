def _update_context(self, context):
    # Dictionary to map field names to x,y,z coordinates
    coord_map = {'E': 'x', 't': 'y', 'phi': 'z'}
    
    # Look for error fields in the graph data
    for field in self.fields:
        # Check if field is an error field (contains 'error' and '_low' or '_high')
        if 'error' in field and ('_low' in field or '_high' in field):
            # Get base field name (remove error_/low/high parts)
            base_field = field.replace('error_', '').replace('_low', '').replace('_high', '')
            
            # Get corresponding coordinate name (x,y,z)
            coord = coord_map.get(base_field, base_field)
            
            # Determine if this is a low or high error
            error_type = 'low' if '_low' in field else 'high'
            
            # Initialize error context if needed
            if 'error' not in context:
                context['error'] = {}
            
            # Get field index
            field_idx = self.fields.index(field)
            
            # Update context with error index
            if f'{coord}_{error_type}' not in context['error']:
                context['error'][f'{coord}_{error_type}'] = {}
            context['error'][f'{coord}_{error_type}']['index'] = field_idx
            
    return context