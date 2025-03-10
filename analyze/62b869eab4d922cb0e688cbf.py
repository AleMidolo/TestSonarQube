def generate_default_observer_schema(app):
    """
    Genera lo schema di osservazione predefinito per ogni risorsa Kubernetes presente in
    ``spec.manifest`` per la quale non è stato specificato uno schema di osservazione personalizzato.

    Argomenti:
        app (krake.data.kubernetes.Application): L'applicazione per la quale generare uno
            schema di osservazione predefinito.
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