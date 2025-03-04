def _update_context(self, context):
    # Get field names from the graph
    fields = self.fields()
    
    # Initialize error context if not exists
    if not hasattr(context, 'error'):
        context.error = {}
        
    # Map coordinate names to x,y,z
    coord_map = {0:'x', 1:'y', 2:'z'}
    
    # Look for error fields in format error_<coord>_low/high
    for field in fields:
        if field.startswith('error_'):
            # Parse error field name
            parts = field.split('_')
            if len(parts) == 3:  # error_coord_direction format
                coord = parts[1]
                direction = parts[2]  # low or high
                
                # Get coordinate index
                for idx, (coord_idx, coord_name) in enumerate(coord_map.items()):
                    if coord == fields[coord_idx]:
                        # Add to error context
                        if coord_name not in context.error:
                            context.error[coord_name] = {}
                        context.error[coord_name][direction] = {'index': fields.index(field)}
                        break
    
    # Preserve existing values in context.value
    if not hasattr(context, 'value'):
        context.value = {}