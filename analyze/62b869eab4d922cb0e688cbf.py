def generate_default_observer_schema(app):
    """
    Generate the default observer schema for each Kubernetes resource present in
    ``spec.manifest`` for which a custom observer schema hasn't been specified.

    Args:
        app (krake.data.kubernetes.Application): The application for which to generate a
            default observer schema
    """
    default_schema = {}
    for resource in app.spec.manifest:
        resource_type = resource.get('kind')
        if resource_type not in app.custom_observer_schemas:
            default_schema[resource_type] = {
                "apiVersion": resource.get('apiVersion'),
                "metadata": {
                    "name": resource.get('metadata', {}).get('name'),
                    "namespace": resource.get('metadata', {}).get('namespace'),
                },
                "spec": resource.get('spec', {})
            }
    return default_schema