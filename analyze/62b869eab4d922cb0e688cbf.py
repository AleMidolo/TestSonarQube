def generate_default_observer_schema(app):
    default_schema = {}
    
    # Check if app has manifest spec
    if not hasattr(app, 'spec') or not hasattr(app.spec, 'manifest'):
        return default_schema

    # Iterate through resources in manifest
    for resource in app.spec.manifest:
        # Skip if resource already has custom observer schema
        if resource.get('metadata', {}).get('name') in getattr(app.spec, 'observer_schema', {}):
            continue
            
        # Get resource kind and name
        kind = resource.get('kind')
        name = resource.get('metadata', {}).get('name')
        
        if not kind or not name:
            continue
            
        # Generate default schema for this resource
        resource_schema = {
            'conditions': [{
                'type': 'Ready',
                'status': 'True'
            }],
            'metrics': {}
        }
        
        # Add schema for common resource types
        if kind.lower() in ['deployment', 'statefulset', 'daemonset']:
            resource_schema['metrics'].update({
                'replicas': {
                    'path': '.status.replicas',
                    'type': 'integer'
                },
                'ready_replicas': {
                    'path': '.status.readyReplicas', 
                    'type': 'integer'
                }
            })
            
        elif kind.lower() == 'service':
            resource_schema['metrics'].update({
                'cluster_ip': {
                    'path': '.spec.clusterIP',
                    'type': 'string'
                }
            })
            
        elif kind.lower() == 'pod':
            resource_schema['metrics'].update({
                'phase': {
                    'path': '.status.phase',
                    'type': 'string'
                }
            })
            
        # Add schema to default_schema dict
        default_schema[name] = resource_schema

    return default_schema