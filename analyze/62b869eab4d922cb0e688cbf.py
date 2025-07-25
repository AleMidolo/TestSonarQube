def generate_default_observer_schema(app):
    """
    为 ``spec.manifest`` 中的每个 Kubernetes 资源生成默认的观察者模式（observer schema），前提是尚未为其指定自定义的观察者模式。

    参数：
        app (krake.data.kubernetes.Application): 需要为其生成默认观察者模式的应用程序。
    """
    if not app.spec.observer:
        app.spec.observer = {}
        
    for resource in app.spec.manifest:
        # 获取资源的 kind 和 apiVersion
        kind = resource.get('kind')
        api_version = resource.get('apiVersion')
        
        # 生成资源的唯一标识符
        resource_id = f"{api_version}/{kind}"
        
        # 如果该资源还没有观察者模式，则生成默认的
        if resource_id not in app.spec.observer:
            default_schema = {
                'apiVersion': api_version,
                'kind': kind,
                'conditions': [
                    {
                        'type': 'Available',
                        'status': 'True'
                    }
                ]
            }
            
            # 为特定类型的资源添加额外的默认条件
            if kind == 'Deployment':
                default_schema['conditions'].append({
                    'type': 'Progressing',
                    'status': 'True'
                })
            elif kind == 'StatefulSet':
                default_schema['conditions'].append({
                    'type': 'Ready',
                    'status': 'True'
                })
            elif kind == 'DaemonSet':
                default_schema['conditions'].append({
                    'type': 'DaemonSetAvailable',
                    'status': 'True'
                })
                
            app.spec.observer[resource_id] = default_schema
            
    return app