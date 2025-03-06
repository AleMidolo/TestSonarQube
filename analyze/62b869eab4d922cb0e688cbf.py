def generate_default_observer_schema(app):
    """
    Generar el esquema de observador predeterminado para cada recurso de Kubernetes presente en  
    ``spec.manifest`` para el cual no se haya especificado un esquema de observador personalizado.

    Argumentos:
    app(krake.data.kubernetes.Application): La aplicación para la cual se generará un esquema de observador predeterminado.
    """
    default_schema = {
        "type": "object",
        "properties": {
            "apiVersion": {"type": "string"},
            "kind": {"type": "string"},
            "metadata": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "namespace": {"type": "string"}
                },
                "required": ["name"]
            },
            "spec": {"type": "object"},
            "status": {"type": "object"}
        },
        "required": ["apiVersion", "kind", "metadata"]
    }

    for resource in app.spec.manifest:
        if not hasattr(resource, 'observer_schema'):
            resource.observer_schema = default_schema

    return app