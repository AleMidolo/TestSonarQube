def generate_default_observer_schema(app):
    default_schema = {}
    
    if hasattr(app, 'spec') and hasattr(app.spec, 'manifest'):
        for resource in app.spec.manifest:
            # Skip if resource already has a custom observer schema
            if resource.get('name') in getattr(app.spec, 'observer_schema', {}):
                continue
                
            # Generate default schema for this resource
            resource_schema = {
                'apiVersion': resource.get('apiVersion'),
                'kind': resource.get('kind'),
                'metadata': {
                    'name': resource.get('metadata', {}).get('name'),
                    'namespace': resource.get('metadata', {}).get('namespace')
                }
            }
            
            # Add schema to default_schema dict using resource name as key
            if resource.get('metadata', {}).get('name'):
                default_schema[resource['metadata']['name']] = resource_schema
    
    return default_schema