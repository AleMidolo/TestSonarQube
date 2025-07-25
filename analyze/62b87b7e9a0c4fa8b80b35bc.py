def _update_context(self, context):
    # Get field names from the graph
    fields = self.fields()
    
    # Initialize error context if not exists
    if not hasattr(context, 'error'):
        context.error = {}
        
    # Map coordinate names to x,y,z
    coord_map = {0: 'x', 1: 'y', 2: 'z'}
    
    # Look for error fields in format error_*_low/high
    for i, field in enumerate(fields):
        if field.startswith('error_'):
            # Parse error field name
            parts = field.split('_')
            if len(parts) >= 3 and parts[-1] in ['low', 'high']:
                # Get coordinate index
                coord_idx = fields.index(parts[1])
                if coord_idx < 3:  # Only handle first 3 coordinates
                    coord_name = coord_map[coord_idx]
                    
                    # Create error entry if not exists
                    if coord_name + '_' + parts[-1] not in context.error:
                        context.error[coord_name + '_' + parts[-1]] = {}
                    
                    # Store field index in context
                    context.error[coord_name + '_' + parts[-1]]['index'] = i
    
    return context