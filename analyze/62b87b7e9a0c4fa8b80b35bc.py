def _update_context(self, context):
    # Get all field names in the graph
    field_names = self.get_field_names()
    
    # Initialize error context if not present
    if not hasattr(context, 'error'):
        context.error = {}

    # Map coordinate names to x,y,z
    coord_map = {0:'x', 1:'y', 2:'z'}
    
    # Look for error fields and add to context
    for field in field_names:
        # Check if field name contains 'error'
        if 'error' in field.lower():
            # Extract coordinate name from error field
            for i, coord in coord_map.items():
                if f'error_{coord}' in field.lower():
                    # Get index of this error field
                    idx = field_names.index(field)
                    
                    # Add to context.error
                    if coord not in context.error:
                        context.error[coord] = {}
                    context.error[coord]['index'] = idx
                    break
            
            # Handle _low/_high variants
            if '_low' in field.lower():
                coord = field.split('_')[1].lower()
                if coord not in context.error:
                    context.error[coord] = {}
                context.error[coord]['index'] = field_names.index(field)
            elif '_high' in field.lower():
                coord = field.split('_')[1].lower() 
                if coord not in context.error:
                    context.error[coord] = {}
                context.error[coord]['index'] = field_names.index(field)

    return context