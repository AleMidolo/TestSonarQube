def view_book_quantity(self, title):
    """
    获取一本书的数量。
    :param title: str, 书名。
    :return quantity: 该书的数量。当书名在 self.inventory 中不存在时返回 0。
    >>> bookManagement = BookManagement()
    >>> bookManagement.add_book("book1", 1)
    >>> bookManagement.view_book_quantity("book3")
    0
    """
    return self.inventory.get(title, 0)