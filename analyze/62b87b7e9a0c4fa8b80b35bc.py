def _update_context(self, context):
    # Dictionary to map field names to x,y,z coordinates
    coord_map = {'E': 'x', 't': 'y', 'phi': 'z'}
    
    # Find error fields in the graph data
    for field in self.fields:
        # Check for error fields (those containing 'error' in name)
        if 'error' in field:
            # Extract base field name and error type
            base_field = field.split('error_')[1].split('_')[0]
            error_type = field.split('_')[-1]  # 'low' or 'high'
            
            # Map to x,y,z coordinate if possible
            coord = coord_map.get(base_field, base_field)
            
            # Initialize error dict if needed
            if 'error' not in context:
                context['error'] = {}
                
            # Create coordinate error dict if needed    
            if coord not in context['error']:
                context['error'][coord] = {}
                
            # Store the index of this error field
            context['error'][coord][error_type] = {'index': self.fields.index(field)}
            
    return context