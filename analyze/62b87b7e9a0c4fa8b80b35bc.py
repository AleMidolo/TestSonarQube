def _update_context(self, context):
    # Get all field names in the graph
    field_names = self.get_field_names()
    
    # Initialize error context if not present
    if not hasattr(context, 'error'):
        context.error = {}

    # Map coordinate names to x,y,z
    coord_names = ['x', 'y', 'z']
    
    # Look for error fields and update context
    for field in field_names:
        # Check if field name contains 'error'
        if 'error' in field.lower():
            # Extract base name before '_error'
            base = field.split('_error')[0].lower()
            
            # Map to x,y,z if possible
            for i, coord in enumerate(coord_names):
                if base == self.get_field_names()[i].lower():
                    base = coord
                    break
                    
            # Get index of error field
            idx = field_names.index(field)
            
            # Add to context.error
            if base + '_low' not in context.error:
                context.error[base + '_low'] = {}
            context.error[base + '_low']['index'] = idx
            
            if base + '_high' not in context.error:
                context.error[base + '_high'] = {}
            context.error[base + '_high']['index'] = idx

    # Preserve existing values in context.value
    if hasattr(context, 'value'):
        pass
        
    return context