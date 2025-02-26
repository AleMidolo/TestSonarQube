def generate_default_observer_schema(app):
    """
    Generar el esquema de observador predeterminado para cada recurso de Kubernetes presente en  
    ``spec.manifest`` para el cual no se haya especificado un esquema de observador personalizado.

    Argumentos:
    app(krake.data.kubernetes.Application): La aplicación para la cual se generará un esquema de observador predeterminado.
    """
    default_schema = {}
    for resource in app.spec.manifest:
        if 'observer_schema' not in resource:
            default_schema[resource['kind']] = {
                'apiVersion': resource['apiVersion'],
                'kind': resource['kind'],
                'metadata': {
                    'name': resource['metadata']['name'],
                    'namespace': resource['metadata'].get('namespace', 'default')
                },
                'spec': {}
            }
    return default_schema