def view_inventory(self):
    """
    获取图书管理系统的库存。
    :return self.inventory: 字典, {标题(str): 数量(int), ...}
    >>> bookManagement = BookManagement()
    >>> bookManagement.add_book("book1", 1)
    >>> bookManagement.add_book("book2", 1)
    >>> bookManagement.view_inventory()
    {'book1': 1, 'book2': 1}
    """
    return self.inventory