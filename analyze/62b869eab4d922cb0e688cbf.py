def generate_default_observer_schema(app):
    default_schema = {}
    for resource in app.spec.manifest:
        if 'observer_schema' not in resource:
            resource_type = resource['kind']
            default_schema[resource_type] = {
                'apiVersion': resource['apiVersion'],
                'kind': resource['kind'],
                'metadata': {
                    'name': resource['metadata']['name'],
                    'namespace': resource['metadata'].get('namespace', 'default')
                },
                'spec': resource.get('spec', {})
            }
    return default_schema