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
        
    # Iterate through each manifest in the application spec
    for manifest in app.spec.manifest:
        # Get the resource kind from the manifest
        kind = manifest.get('kind')
        
        # Skip if kind is not present
        if not kind:
            continue
            
        # Skip if observer schema already exists for this kind
        if kind in app.spec.observer:
            continue
            
        # Generate default schema based on resource kind
        default_schema = {
            'conditions': [{
                'type': 'Available',
                'status': 'True'
            }],
            'state': {
                'ready': {
                    'path': 'status.conditions[?type=="Ready"].status',
                    'value': 'True'
                }
            }
        }
        
        # Add default schema to observer
        app.spec.observer[kind] = default_schema