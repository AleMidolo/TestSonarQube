def _update_context(self, context):
    # Get field names from the graph
    fields = self.fields()
    
    # Initialize error context if not exists
    if not hasattr(context, 'error'):
        context.error = {}
        
    # Map coordinate names to x,y,z
    coord_map = {0: 'x', 1: 'y', 2: 'z'}
    
    # Look for error fields in format "error_<field>_low/high"
    for field in fields:
        if field.startswith('error_'):
            # Parse error field name
            parts = field.split('_')
            if len(parts) >= 3 and parts[-1] in ['low', 'high']:
                # Get base field name
                base_field = '_'.join(parts[1:-1])
                
                # Find index of base field
                try:
                    base_idx = fields.index(base_field)
                    # Map to x,y,z if applicable
                    error_name = coord_map.get(base_idx, base_field)
                    
                    # Update context
                    if error_name not in context.error:
                        context.error[error_name] = {}
                    context.error[error_name][parts[-1]] = {
                        'index': fields.index(field)
                    }
                except ValueError:
                    # Base field not found, skip
                    continue
    
    return context