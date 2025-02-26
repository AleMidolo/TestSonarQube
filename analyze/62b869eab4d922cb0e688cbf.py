def generate_default_observer_schema(app):
    """
    为 ``spec.manifest`` 中的每个 Kubernetes 资源生成默认的观察者模式（observer schema），前提是尚未为其指定自定义的观察者模式。

    参数：
        app (krake.data.kubernetes.Application): 需要为其生成默认观察者模式的应用程序。
    """
    for resource in app.spec.manifest:
        if not hasattr(resource, 'observer_schema'):
            resource.observer_schema = create_default_observer_schema(resource)
    return app

def create_default_observer_schema(resource):
    # 这里可以根据资源类型生成默认的观察者模式
    return {
        "type": resource.kind,
        "version": resource.apiVersion,
        "metadata": {
            "name": resource.metadata.name,
            "namespace": resource.metadata.namespace
        }
    }