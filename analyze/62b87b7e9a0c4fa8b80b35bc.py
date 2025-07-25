def _update_context(self, context):
    # Map field names to error names (x, y, z)
    error_name_map = {
        'E': 'x',
        't': 'y',
        'phi': 'z'
    }
    
    # Get all field names from the graph
    field_names = [f for f in self.fields]
    
    # Initialize error context if not present
    if not hasattr(context, 'error'):
        context.error = {}
        
    # Look for error fields (those containing "error" in name)
    for field in field_names:
        if 'error' in field.lower():
            # Parse the error field name to get base field and bound
            parts = field.split('_')
            base_field = parts[1]  # E.g. 'E' from 'error_E_low'
            bound = parts[-1]      # E.g. 'low' from 'error_E_low'
            
            # Map base field to x/y/z if possible
            error_name = error_name_map.get(base_field, base_field)
            
            # Create error entry
            error_key = f"{error_name}_{bound}"
            if error_key not in context.error:
                context.error[error_key] = {}
                
            # Store index of error field
            context.error[error_key]['index'] = field_names.index(field)
            
    return context