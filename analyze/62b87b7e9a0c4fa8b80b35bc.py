def _update_context(self, context):
    # Dictionary to map field positions to x,y,z labels
    coord_names = {0: 'x', 1: 'y', 2: 'z'}
    
    # Initialize error context if it doesn't exist
    if not hasattr(context, 'error'):
        context.error = {}
        
    # Iterate through field names looking for error fields
    for i, field in enumerate(self.fields):
        # Check if field name contains 'error'
        if 'error' in field.lower():
            # Determine if it's a low or high error
            error_type = 'low' if 'low' in field.lower() else 'high'
            
            # Get corresponding coordinate name (x,y,z) based on position
            if i < 3:
                coord = coord_names[i]
                
                # Create error entry with index
                error_key = f"{coord}_{error_type}"
                context.error[error_key] = {"index": i}
                
    return context