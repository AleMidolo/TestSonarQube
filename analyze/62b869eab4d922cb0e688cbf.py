def generate_default_observer_schema(app):
    """
    为 ``spec.manifest`` 中的每个 Kubernetes 资源生成默认的观察者模式（observer schema），前提是尚未为其指定自定义的观察者模式。

    参数：
        app (krake.data.kubernetes.Application): 需要为其生成默认观察者模式的应用程序。
    """
    for resource in app.spec.manifest:
        if not hasattr(resource, 'observer_schema'):
            resource.observer_schema = generate_schema_for_resource(resource)
    return app

def generate_schema_for_resource(resource):
    # 这里可以根据资源的类型生成相应的默认观察者模式
    return {
        "type": resource.kind,
        "properties": {
            "status": {
                "type": "object",
                "properties": {
                    "availableReplicas": {"type": "integer"},
                    "conditions": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {"type": "string"},
                                "status": {"type": "string"},
                                "reason": {"type": "string"},
                                "message": {"type": "string"},
                                "lastTransitionTime": {"type": "string", "format": "date-time"},
                            }
                        }
                    }
                }
            }
        }
    }