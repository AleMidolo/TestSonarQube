def _update_context(self, context):
    # Map field names to error names (x, y, z)
    error_name_map = {
        'E': 'x',
        't': 'y',
        'phi': 'z'
    }
    
    # Get all field names from the graph
    fields = self.get_fields()
    
    # Initialize error context if not present
    if not hasattr(context, 'error'):
        context.error = {}
        
    # Look for error fields (those containing "error" in name)
    for field in fields:
        if 'error' not in field:
            continue
            
        # Parse error field name to get base field and error type
        parts = field.split('_')
        base_field = parts[0]
        error_type = '_'.join(parts[2:]) # e.g. 'low', 'high'
        
        # Map base field to x/y/z if possible
        if base_field in error_name_map:
            error_name = error_name_map[base_field]
        else:
            error_name = base_field
            
        # Get index of this field
        field_index = fields.index(field)
        
        # Create nested error context structure
        if error_name not in context.error:
            context.error[error_name] = {}
            
        # Add error index to context
        error_key = f"{error_type}"
        context.error[error_name][error_key] = {"index": field_index}
        
    return context