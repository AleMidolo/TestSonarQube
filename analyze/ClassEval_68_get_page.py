def get_page(self, page_number):
    """
    获取特定页面的数据。
    :param page_number: int, 要获取的页面编号
    :return: list, 指定页面上的数据
    >>> page_util = PageUtil([1, 2, 3, 4], 1)
    >>> page_util.get_page(1)
    [1]

    """
    if not hasattr(self, 'data') or not hasattr(self, 'page_size'):
        return []
    
    if page_number < 1:
        return []
    
    start_index = (page_number - 1) * self.page_size
    end_index = start_index + self.page_size
    
    if start_index >= len(self.data):
        return []
    
    return self.data[start_index:end_index]