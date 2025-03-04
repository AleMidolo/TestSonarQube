def generate_default_observer_schema(app):
    default_schema = {}
    
    # Iterate through each resource in the application manifest
    for resource in app.spec.manifest:
        # Skip if resource already has custom observer schema defined
        if resource.get('observer_schema'):
            continue
            
        # Get resource kind and API version
        kind = resource.get('kind', '')
        api_version = resource.get('apiVersion', '')
        
        # Generate default schema based on resource kind
        if kind.lower() == 'deployment':
            default_schema[f"{api_version}/{kind}"] = {
                'ready': '$.status.readyReplicas == $.spec.replicas'
            }
        elif kind.lower() == 'statefulset':
            default_schema[f"{api_version}/{kind}"] = {
                'ready': '$.status.readyReplicas == $.spec.replicas'
            }
        elif kind.lower() == 'daemonset':
            default_schema[f"{api_version}/{kind}"] = {
                'ready': '$.status.numberReady == $.status.desiredNumberScheduled'
            }
        elif kind.lower() == 'pod':
            default_schema[f"{api_version}/{kind}"] = {
                'ready': "$.status.phase in ['Running', 'Succeeded']"
            }
        elif kind.lower() == 'service':
            default_schema[f"{api_version}/{kind}"] = {
                'ready': 'true'
            }
        elif kind.lower() == 'persistentvolumeclaim':
            default_schema[f"{api_version}/{kind}"] = {
                'ready': "$.status.phase == 'Bound'"
            }
        else:
            # Default schema for other resource types
            default_schema[f"{api_version}/{kind}"] = {
                'ready': 'true'
            }
            
    return default_schema