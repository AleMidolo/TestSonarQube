def add_book(self, title, author):
    """
    将一本书添加到数据库中，指定书名和作者，
    将其可借阅状态设置为1，表示可以借阅。
    :param title: str, 书名
    :param author: str, 作者姓名
    >>> book_db = BookManagementDB("test.db")
    >>> book_db.create_table()
    >>> book_db.add_book('book1', 'author')
    """
    cursor = self.connection.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, available) VALUES (?, ?, ?)",
        (title, author, 1)
    )
    self.connection.commit()