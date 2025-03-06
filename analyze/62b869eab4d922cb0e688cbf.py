def generate_default_observer_schema(app):
    """
    为 ``spec.manifest`` 中的每个 Kubernetes 资源生成默认的观察者模式（observer schema），前提是尚未为其指定自定义的观察者模式。

    参数：
      app (krake.data.kubernetes.Application): 需要为其生成默认观察者模式的应用程序。
    """
    for resource in app.spec.manifest:
        if not hasattr(resource, 'observer_schema'):
            # 生成默认的观察者模式
            resource.observer_schema = {
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
    return app