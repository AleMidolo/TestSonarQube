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
                base_field = parts[1]
                error_type = parts[-1]
                
                # Get index of base field
                try:
                    base_index = self.fields.index(base_field)
                    # Map to x,y,z if index is 0,1,2
                    if base_index in coord_names:
                        coord = coord_names[base_index]
                        
                        # Create nested error structure
                        if coord not in context.error:
                            context.error[coord] = {}
                        context.error[coord][error_type] = {'index': self.fields.index(field_name)}
                except ValueError:
                    # Base field not found, skip
                    continue
                    
    return context