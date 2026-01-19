def __init__(self, db_name):
    """
    初始化数据库处理器
    :param db_name: 数据库文件名
    """
    self.db_name = db_name
    self.connection = None