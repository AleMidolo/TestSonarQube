def generate_default_observer_schema(app):
    default_schema = {}
    
    # Check if app has manifest spec
    if not hasattr(app, 'spec') or not hasattr(app.spec, 'manifest'):
        return default_schema

    # Iterate through each resource in manifest
    for resource in app.spec.manifest:
        # Skip if resource already has custom observer schema
        if resource.get('observer_schema'):
            continue
            
        # Get resource kind and API version
        kind = resource.get('kind', '')
        api_version = resource.get('apiVersion', '')
        
        # Generate default schema based on resource kind
        if kind.lower() in ['deployment', 'statefulset', 'daemonset']:
            default_schema[f"{api_version}/{kind}"] = {
                'ready': {
                    'path': '.status.readyReplicas',
                    'type': 'integer'
                },
                'total': {
                    'path': '.status.replicas', 
                    'type': 'integer'
                }
            }
        elif kind.lower() == 'pod':
            default_schema[f"{api_version}/{kind}"] = {
                'ready': {
                    'path': '.status.containerStatuses[*].ready',
                    'type': 'boolean'
                },
                'phase': {
                    'path': '.status.phase',
                    'type': 'string'
                }
            }
        elif kind.lower() == 'service':
            default_schema[f"{api_version}/{kind}"] = {
                'ready': {
                    'path': '.spec.clusterIP',
                    'type': 'string'
                }
            }
            
    return default_schema