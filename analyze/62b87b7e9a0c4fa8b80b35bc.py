def _update_context(self, context):
    # Initialize error dict if it doesn't exist
    if not hasattr(context, 'error'):
        context.error = {}

    # Map field names to error coordinate names (x,y,z)
    coord_map = {0: 'x', 1: 'y', 2: 'z'}
    
    # Get list of field names
    fields = self.fields.split(',')
    
    # Look for error fields
    for i, field in enumerate(fields):
        if field.startswith('error_'):
            # Extract base field name and error type
            base_field = field[6:].split('_')[0] 
            error_type = field[6:].split('_')[1] if '_' in field[6:] else ''
            
            # Find index of base field
            try:
                base_idx = fields.index(base_field)
                if base_idx <= 2:  # Only handle first 3 coordinates
                    coord_name = coord_map[base_idx]
                    
                    # Create error entry
                    if coord_name not in context.error:
                        context.error[coord_name] = {}
                    
                    # Add error index
                    error_key = f"{error_type}" if error_type else "index"
                    context.error[coord_name][error_key] = i
                    
            except ValueError:
                # Base field not found, skip
                continue
                
    return context