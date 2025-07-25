def _update_context(self, context):
    # Get field names from the graph
    fields = self.fields()
    
    # Initialize error dict if not exists
    if not hasattr(context, 'error'):
        context.error = {}
        
    # Map coordinate names to x,y,z
    coord_map = {0:'x', 1:'y', 2:'z'}
    
    # Look for error fields
    for field in fields:
        if 'error' in field.lower():
            # Extract base coordinate name and error type
            parts = field.split('_')
            if len(parts) >= 3 and parts[-2] == 'error':
                coord = parts[0]
                error_type = parts[-1]  # low/high
                
                # Find index of this field
                try:
                    idx = fields.index(field)
                    
                    # Map coordinate to x,y,z if possible
                    try:
                        coord_idx = fields.index(coord)
                        if coord_idx <= 2:  # Only map first 3 coordinates
                            coord = coord_map[coord_idx]
                    except ValueError:
                        pass
                        
                    # Update context
                    error_key = f"{coord}_{error_type}"
                    if error_key not in context.error:
                        context.error[error_key] = {}
                    context.error[error_key]['index'] = idx
                        
                except ValueError:
                    continue
                    
    return context