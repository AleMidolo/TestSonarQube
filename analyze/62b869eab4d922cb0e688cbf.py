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
            "status": {
                "type": "object",
                "properties": {
                    "conditions": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {"type": "string"},
                                "status": {"type": "string"},
                                "lastTransitionTime": {"type": "string"},
                                "reason": {"type": "string"},
                                "message": {"type": "string"}
                            },
                            "required": ["type", "status"]
                        }
                    }
                },
                "required": ["conditions"]
            }
        },
        "required": ["status"]
    }

    for resource in app.spec.manifest:
        if not hasattr(resource, 'observer_schema'):
            resource.observer_schema = default_schema

    return app