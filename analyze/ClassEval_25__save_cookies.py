import json
import os

def _save_cookies(self):
    """
    将 cookies 保存到 cookies_file，并在成功时返回 True，否则返回 False。
    :return: 成功时返回 True，否则返回 False。
    >>> cookies_util = CookiesUtil('cookies.json')
    >>> cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
    >>> cookies_util._save_cookies()
    True

    """
    try:
        # 确保目录存在
        directory = os.path.dirname(self.cookies_file)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        # 将 cookies 保存到文件
        with open(self.cookies_file, 'w', encoding='utf-8') as f:
            json.dump(self.cookies, f, ensure_ascii=False, indent=4)
        
        return True
    except Exception as e:
        # 如果发生任何异常，返回 False
        return False