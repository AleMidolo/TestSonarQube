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
            if len(parts) >= 3:
                coord = parts[1]  # E.g. 'E' from 'error_E_low'
                error_type = parts[2]  # E.g. 'low'
                
                # Find coordinate index
                try:
                    coord_idx = fields.index(coord)
                    if coord_idx <= 2:  # Only handle first 3 coordinates
                        coord_name = coord_map[coord_idx]
                        
                        # Create nested dict structure
                        if coord_name not in context.error:
                            context.error[coord_name] = {}
                            
                        # Store error field index
                        error_key = f"{error_type}"
                        context.error[coord_name][error_key] = {"index": fields.index(field)}
                except ValueError:
                    pass  # Coordinate field not found
                    
    return context