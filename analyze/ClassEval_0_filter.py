def __init__(self):
    """初始化访问网关过滤器，设置允许的路径和方法规则"""
    # 定义允许的路径和方法组合
    self.allowed_rules = {
        '/login': ['POST', 'GET'],
        '/logout': ['POST'],
        '/register': ['POST'],
        '/home': ['GET'],
        '/api/data': ['GET', 'POST', 'PUT', 'DELETE'],
        '/public': ['GET'],
    }

    # 定义公开路径（不需要验证）
    self.public_paths = ['/login', '/register', '/public']

    # 定义黑名单路径
    self.blacklist_paths = ['/admin/delete', '/system/config']