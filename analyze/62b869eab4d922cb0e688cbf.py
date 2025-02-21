def generate_default_observer_schema(app):
    """
    Genera lo schema di osservazione predefinito per ogni risorsa Kubernetes presente in
    ``spec.manifest`` per la quale non è stato specificato uno schema di osservazione personalizzato.

    Argomenti:
        app (krake.data.kubernetes.Application): L'applicazione per la quale generare uno
            schema di osservazione predefinito.
    """
    default_schema = {}
    for resource in app.spec.manifest:
        if not resource.get('custom_observer_schema'):
            resource_type = resource['kind'].lower()
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