def _update_context(self, context):
    # Dictionary to map field indices to x,y,z labels
    coord_names = {0: 'x', 1: 'y', 2: 'z'}
    
    # Initialize error context if it doesn't exist
    if not hasattr(context, 'error'):
        context.error = {}
        
    # Look through field names for error fields
    for field_name in self.fields:
        # Check if field name contains 'error'
        if 'error' in field_name.lower():
            # Extract base field name and error type (low/high)
            parts = field_name.split('_')
            if len(parts) >= 3 and parts[-1] in ['low', 'high']:
                base_field = parts[1]  # E in error_E_low
                error_type = parts[-1] # low/high
                
                # Get index of base field
                try:
                    field_idx = self.fields.index(base_field)
                    
                    # Map to x,y,z if index is 0,1,2
                    if field_idx in coord_names:
                        base_field = coord_names[field_idx]
                        
                    # Create nested structure in context.error
                    if base_field not in context.error:
                        context.error[base_field] = {}
                    
                    # Add error index
                    error_key = f"{base_field}_{error_type}"
                    context.error[base_field][error_type] = {
                        "index": self.fields.index(field_name)
                    }
                except ValueError:
                    # Base field not found, skip
                    continue