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
                if base == coord:
                    base = coord
                    break
                    
            # Get index of this field
            idx = field_names.index(field)
            
            # Add to error context
            if base not in context.error:
                context.error[base] = {}
            context.error[base]['index'] = idx

    # Preserve existing values in context.value
    if hasattr(context, 'value'):
        pass