def generate_default_observer_schema(app):
    """
    Generate the default observer schema for each Kubernetes resource present in
    ``spec.manifest`` for which a custom observer schema hasn't been specified.

    Args:
        app (krake.data.kubernetes.Application): The application for which to generate a
            default observer schema
    """
    default_schema = {
        "apiVersion": "v1",
        "kind": "ObserverSchema",
        "metadata": {
            "name": "default-observer-schema",
            "namespace": app.metadata.namespace
        },
        "spec": {
            "resources": []
        }
    }

    for resource in app.spec.manifest:
        resource_schema = {
            "group": resource.get("group", ""),
            "version": resource.get("version", "v1"),
            "kind": resource.get("kind", ""),
            "namespace": resource.get("metadata", {}).get("namespace", ""),
            "name": resource.get("metadata", {}).get("name", ""),
            "observer": {
                "type": "status",
                "status": {
                    "conditions": [
                        {
                            "type": "Ready",
                            "status": "True"
                        }
                    ]
                }
            }
        }
        default_schema["spec"]["resources"].append(resource_schema)

    return default_schema