def __init__(self, file_name):
    """
    初始化XMLProcessor对象
    :param file_name: 字符串，XML文件名
    """
    self.file_name = file_name
    self.tree = None
    self.root = None