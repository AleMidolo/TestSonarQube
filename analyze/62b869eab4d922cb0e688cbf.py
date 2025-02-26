def generate_default_observer_schema(app):
    """
    为 ``spec.manifest`` 中的每个 Kubernetes 资源生成默认的观察者模式（observer schema），前提是尚未为其指定自定义的观察者模式。

    参数：
        app (krake.data.kubernetes.Application): 需要为其生成默认观察者模式的应用程序。
    """
    default_schema = {}
    
    for resource in app.spec.manifest:
        if 'observer' not in resource:
            default_schema[resource['kind']] = {
                'apiVersion': resource['apiVersion'],
                'kind': resource['kind'],
                'metadata': {
                    'name': resource['metadata']['name'],
                    'namespace': resource['metadata'].get('namespace', 'default')
                },
                'spec': {
                    # Add default spec fields based on resource kind
                }
            }
    
    return default_schema