def _update_context(self, context):
    # Get field names from the graph
    fields = self.fields()
    
    # Initialize error context if not exists
    if not hasattr(context, 'error'):
        context.error = {}
        
    # Map coordinate names to x,y,z
    coord_map = {0: 'x', 1: 'y', 2: 'z'}
    
    # Look for error fields in format error_<coord>_low/high
    for field in fields:
        if field.startswith('error_'):
            # Parse error field name
            parts = field.split('_')
            if len(parts) == 3:  # error_<coord>_<direction>
                coord = parts[1]
                direction = parts[2]  # low or high
                
                # Find index of this error field
                try:
                    field_idx = fields.index(field)
                except ValueError:
                    continue
                    
                # Map coordinate name if it's one of first 3
                try:
                    coord_idx = fields.index(coord)
                    if coord_idx < 3:
                        coord = coord_map[coord_idx]
                except ValueError:
                    pass
                
                # Update context with error index
                if coord not in context.error:
                    context.error[coord] = {}
                context.error[coord][direction] = {"index": field_idx}
                
    return context