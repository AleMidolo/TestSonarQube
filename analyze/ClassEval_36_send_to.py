def __init__(self, email, capacity):
    """
    初始化邮件客户端
    :param email: 邮箱地址
    :param capacity: 邮箱容量
    """
    self.email = email
    self.capacity = capacity
    self.inbox = []
    self.current_size = 0