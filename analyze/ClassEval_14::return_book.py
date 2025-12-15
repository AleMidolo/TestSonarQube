def return_book(self, book_id):
        """
        根据给定的书籍ID在数据库中标记书籍为已归还。
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.return_book(1)
        """
        self.cursor.execute('''
                UPDATE books SET available = 1 WHERE id = ?
            ''', (book_id,))
        self.connection.commit()