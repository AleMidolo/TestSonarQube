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
                    "resource": {
                        "apiVersion": "*",
                        "kind": "*"
                    },
                    "observation": {
                        "interval": "60s",
                        "timeout": "30s",
                        "successThreshold": 1,
                        "failureThreshold": 3
                    }
                }
            ]
        }
    }

    # Aggiungi lo schema di osservazione predefinito all'applicazione
    if not hasattr(app.spec, 'observerSchemas'):
        app.spec.observerSchemas = []
    
    app.spec.observerSchemas.append(default_schema)