def __init__(self, cookies_file):
    """
    初始化 CookiesUtil 类
    :param cookies_file: cookies 文件路径
    """
    self.cookies_file = cookies_file
    self.cookies = {}