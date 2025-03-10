def generate_default_observer_schema(app):
    """
    Generate the default observer schema for each Kubernetes resource present in
    ``spec.manifest`` for which a custom observer schema hasn't been specified.

    Args:
        app (krake.data.kubernetes.Application): The application for which to generate a
            default observer schema
    """
    if not app.spec.manifest:
        return

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
                            }
                        }
                    }
                }
            }
        }
    }

    for resource in app.spec.manifest:
        if not hasattr(resource, 'observer_schema') or not resource.observer_schema:
            resource.observer_schema = default_schema