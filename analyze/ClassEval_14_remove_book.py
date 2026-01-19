def __init__(self, db_name):
    """初始化数据库连接"""
    self.db_name = db_name
    self.connection = sqlite3.connect(db_name)
    self.cursor = self.connection.cursor()
    self._create_table()