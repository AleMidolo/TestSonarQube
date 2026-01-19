def get_mode(self):
    """
    获取当前工作模式
    :return mode: str, 工作模式。仅限 ['heat', 'cool']
    """
    if not hasattr(self, '_mode'):
        self._mode = 'cool'  # 默认模式为制冷
    return self._mode