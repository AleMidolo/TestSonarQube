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
        resource_type = resource.get('kind')
        if resource_type not in default_schema:
            default_schema[resource_type] = {
                'apiVersion': resource.get('apiVersion'),
                'metadata': {
                    'name': resource['metadata'].get('name'),
                    'namespace': resource['metadata'].get('namespace')
                },
                'spec': resource.get('spec', {})
            }
    
    return default_schema