def _update_context(self, context):
    # Map field names to error names (x, y, z)
    error_name_map = {
        'E': 'x',
        't': 'y',
        'phi': 'z'
    }
    
    # Look through fields for error fields
    for field in self.fields:
        # Check if field is an error field by looking for "error_" prefix
        if field.startswith('error_'):
            # Parse the error field name to get base field and error type
            parts = field.split('_')
            base_field = parts[1]
            error_type = '_'.join(parts[2:]) # Join remaining parts for error type
            
            # Get the error name (x,y,z) for this field
            error_name = error_name_map.get(base_field)
            
            if error_name:
                # Initialize error dict if needed
                if not hasattr(context, 'error'):
                    context.error = {}
                    
                # Create error subcontext
                error_key = f"{error_name}_{error_type}"
                if error_key not in context.error:
                    context.error[error_key] = {}
                    
                # Store the field index in the error subcontext
                context.error[error_key]['index'] = self.fields.index(field)