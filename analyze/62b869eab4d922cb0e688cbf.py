def generate_default_observer_schema(app):
    """
    Generate the default observer schema for each Kubernetes resource present in
    ``spec.manifest`` for which a custom observer schema hasn't been specified.

    Args:
        app (krake.data.kubernetes.Application): The application for which to generate a
            default observer schema
    """
    # Initialize empty observer schema if none exists
    if not app.spec.observer:
        app.spec.observer = {}
        
    # Iterate through each resource in the manifest
    for resource in app.spec.manifest:
        # Get resource kind and API version
        kind = resource.get('kind')
        api_version = resource.get('apiVersion')
        
        # Skip if resource already has custom observer schema
        if f"{api_version}/{kind}" in app.spec.observer:
            continue
            
        # Generate default schema based on resource kind
        default_schema = {
            'conditions': [{
                'type': 'Available',
                'status': 'True'
            }]
        }
        
        # Add specific defaults for common resource types
        if kind == 'Deployment':
            default_schema['conditions'].append({
                'type': 'Progressing',
                'status': 'True'
            })
        elif kind == 'StatefulSet':
            default_schema['conditions'].append({
                'type': 'Ready',
                'status': 'True' 
            })
        elif kind == 'DaemonSet':
            default_schema['conditions'].append({
                'type': 'DaemonSetAvailable',
                'status': 'True'
            })
            
        # Add generated schema to observer
        app.spec.observer[f"{api_version}/{kind}"] = default_schema