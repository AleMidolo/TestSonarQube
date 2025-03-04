def generate_default_observer_schema(app):
    default_schema = {}
    
    # Check if app has manifest spec
    if not hasattr(app, 'spec') or not hasattr(app.spec, 'manifest'):
        return default_schema

    # Iterate through resources in manifest
    for resource in app.spec.manifest:
        # Skip if resource already has custom observer schema
        if resource.get('observer_schema'):
            continue
            
        # Get resource kind and API version
        kind = resource.get('kind')
        api_version = resource.get('apiVersion')
        
        if not kind or not api_version:
            continue
            
        # Generate default schema for this resource type
        resource_schema = {
            'type': 'object',
            'properties': {
                'status': {
                    'type': 'object',
                    'properties': {
                        'phase': {'type': 'string'},
                        'conditions': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'status': {'type': 'string'},
                                    'reason': {'type': 'string'},
                                    'message': {'type': 'string'}
                                }
                            }
                        }
                    }
                }
            }
        }
        
        # Add schema to default_schema dict with resource type as key
        resource_key = f"{api_version}/{kind}"
        default_schema[resource_key] = resource_schema

    return default_schema