def _update_context(self, context):
    # Get field names from the graph
    fields = self.fields()
    
    # Initialize error dict if not exists
    if not hasattr(context, 'error'):
        context.error = {}
        
    # Map coordinate names to x,y,z
    coord_map = {0: 'x', 1: 'y', 2: 'z'}
    
    # Look for error fields
    for field in fields:
        if 'error' in field.lower():
            # Extract base field name and error type
            parts = field.split('_')
            if len(parts) >= 3 and parts[-2] == 'error':
                base_field = parts[0]
                error_type = parts[-1]  # low/high
                
                # Find index of base field
                try:
                    base_idx = fields.index(base_field)
                    coord_name = coord_map.get(base_idx)
                    
                    if coord_name:
                        # Create error entry if not exists
                        if coord_name not in context.error:
                            context.error[coord_name] = {}
                            
                        # Add error field index
                        error_key = f"{coord_name}_{error_type}"
                        field_idx = fields.index(field)
                        context.error[coord_name][error_type] = {"index": field_idx}
                        
                except ValueError:
                    # Base field not found, skip
                    continue
                    
    return context