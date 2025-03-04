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
            
        # Get resource kind
        kind = resource.get('kind', '')
        
        # Generate default schema based on resource kind
        if kind == 'Deployment':
            default_schema[resource['metadata']['name']] = {
                'ready': '$.status.readyReplicas == $.spec.replicas'
            }
        elif kind == 'StatefulSet':
            default_schema[resource['metadata']['name']] = {
                'ready': '$.status.readyReplicas == $.spec.replicas'
            }
        elif kind == 'DaemonSet':
            default_schema[resource['metadata']['name']] = {
                'ready': '$.status.numberReady == $.status.desiredNumberScheduled'
            }
        elif kind == 'Pod':
            default_schema[resource['metadata']['name']] = {
                'ready': "$.status.phase in ['Running', 'Succeeded']"
            }
        elif kind == 'Service':
            default_schema[resource['metadata']['name']] = {
                'ready': 'true'
            }
        elif kind == 'PersistentVolumeClaim':
            default_schema[resource['metadata']['name']] = {
                'ready': "$.status.phase == 'Bound'"
            }
        elif kind == 'Job':
            default_schema[resource['metadata']['name']] = {
                'ready': "$.status.succeeded == 1"
            }
        elif kind == 'CronJob':
            default_schema[resource['metadata']['name']] = {
                'ready': 'true'
            }
            
    return default_schema