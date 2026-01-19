def __init__(self):
    """初始化访问网关过滤器，设置允许的路径和方法规则"""
    # 定义允许的路径和方法组合
    self.allowed_rules = {
        '/login': ['POST', 'GET'],
        '/register': ['POST'],
        '/home': ['GET'],
        '/api/data': ['GET', 'POST', 'PUT', 'DELETE'],
        '/logout': ['POST', 'GET'],
        '/public': ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
    }

    # 定义公共路径前缀（无需验证）
    self.public_prefixes = ['/public', '/static', '/assets']

    # 定义黑名单路径
    self.blacklist_paths = ['/admin/delete', '/system/shutdown']