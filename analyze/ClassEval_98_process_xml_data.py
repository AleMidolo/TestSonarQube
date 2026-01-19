def __init__(self, file_path):
    """
    初始化XMLProcessor类
    :param file_path: XML文件的路径
    """
    self.file_path = file_path
    self.tree = None
    self.root = None