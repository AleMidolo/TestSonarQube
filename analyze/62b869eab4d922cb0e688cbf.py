def generate_default_observer_schema(app):
    default_schema = {}
    
    if hasattr(app, 'spec') and hasattr(app.spec, 'manifest'):
        for resource in app.spec.manifest:
            # Skip if resource already has a custom observer schema
            if resource.get('metadata', {}).get('name') in app.spec.get('observer_schema', {}):
                continue
                
            # Generate default schema for each resource
            resource_name = resource.get('metadata', {}).get('name')
            if resource_name:
                default_schema[resource_name] = {
                    'ready': {
                        'path': 'status.conditions[?(@.type=="Ready")].status',
                        'value': 'True'
                    },
                    'available': {
                        'path': 'status.conditions[?(@.type=="Available")].status',
                        'value': 'True'
                    }
                }
    
    return default_schema