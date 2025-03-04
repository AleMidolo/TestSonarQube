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
            if len(parts) >= 3 and parts[-1] in ['low', 'high']:
                base_coord = parts[-2]
                error_type = parts[-1]
                
                # Find index of base coordinate in fields
                try:
                    coord_idx = fields.index(base_coord)
                    if coord_idx <= 2:  # Only handle first 3 coordinates
                        coord_name = coord_map[coord_idx]
                        
                        # Create error entry if not exists
                        if coord_name not in context.error:
                            context.error[coord_name] = {}
                            
                        # Store error field index
                        error_key = f"{coord_name}_{error_type}"
                        context.error[coord_name][error_type] = {"index": fields.index(field)}
                except ValueError:
                    continue
    
    return context