def _update_context(self, context):
    # Get all field names in the graph
    field_names = self.get_field_names()
    
    # Initialize error context if not present
    if not hasattr(context, 'error'):
        context.error = {}

    # Map coordinate names to x,y,z
    coord_map = {'E': 'x', 't': 'y', 'phi': 'z'}
    
    # Look for error fields and add to context
    for field in field_names:
        # Check if field name contains 'error'
        if 'error' in field.lower():
            # Extract base coordinate name (before _error)
            base = field.split('_error')[0]
            
            # Get mapped coordinate name (x,y,z) if exists
            coord_name = coord_map.get(base, base)
            
            # Add error field index to context
            if '_low' in field:
                if coord_name not in context.error:
                    context.error[coord_name] = {}
                context.error[coord_name]['index'] = field_names.index(field)
                
            elif '_high' in field:
                if coord_name not in context.error:
                    context.error[coord_name] = {}
                context.error[coord_name]['index'] = field_names.index(field)
    
    # Preserve existing values in context.value
    if hasattr(context, 'value'):
        pass