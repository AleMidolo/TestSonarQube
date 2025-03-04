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
            # e.g. error_E_low -> E
            coord = field.split('_')[1]
            
            # Map to x,y,z if possible
            try:
                coord_idx = field_names.index(coord)
                if coord_idx < 3:  # Only map first 3 coordinates
                    coord = coord_map[coord_idx]
            except:
                pass
                
            # Add error field index to context
            error_name = f"{coord}_low" if "low" in field.lower() else f"{coord}_high"
            if error_name not in context.error:
                context.error[error_name] = {}
            context.error[error_name]["index"] = field_names.index(field)
            
    return context