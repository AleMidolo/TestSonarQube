def generate_default_observer_schema(app):
    """
    Genera lo schema di osservazione predefinito per ogni risorsa Kubernetes presente in
    ``spec.manifest`` per la quale non è stato specificato uno schema di osservazione personalizzato.

    Argomenti:
        app (krake.data.kubernetes.Application): L'applicazione per la quale generare uno
            schema di osservazione predefinito.
    """
    default_schema = {
        "apiVersion": "v1",
        "kind": "ObserverSchema",
        "metadata": {
            "name": "default-observer-schema",
            "namespace": app.metadata.namespace
        },
        "spec": {
            "rules": [
                {
                    "apiGroups": ["*"],
                    "resources": ["*"],
                    "verbs": ["get", "list", "watch"]
                }
            ]
        }
    }

    for resource in app.spec.manifest:
        if not hasattr(resource, 'observer_schema'):
            resource.observer_schema = default_schema

    return app