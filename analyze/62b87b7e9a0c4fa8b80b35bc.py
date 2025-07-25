def _update_context(self, context):
    # Dictionary to map field names to x,y,z coordinates
    coord_map = {'E': 'x', 't': 'y', 'phi': 'z'}
    
    # Find error fields in the graph
    for field in self.fields:
        # Check if field has error components
        if field.startswith('error_'):
            # Extract base field name and error type
            base_field, error_type = field.split('error_')[1].split('_')
            
            # Map the base field to x,y,z coordinate name
            if base_field in coord_map:
                coord_name = coord_map[base_field]
                
                # Initialize error dict if needed
                if 'error' not in context:
                    context['error'] = {}
                    
                # Add error index to context
                error_key = f"{coord_name}_{error_type}"
                if error_key not in context['error']:
                    context['error'][error_key] = {}
                    
                # Store the field index
                context['error'][error_key]['index'] = self.fields.index(field)
                
    return context