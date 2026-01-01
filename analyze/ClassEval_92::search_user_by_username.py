def search_user_by_username(self, username):
    """
        根据用户名在“users”表中搜索用户。
        :param username: str，要搜索的用户的用户名。
        :return: 元组的列表，符合搜索条件的“users”表中的行。
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> result = user_db.search_user_by_username('user1')
        len(result) = 1
        """
    self.cursor.execute('\n            SELECT * FROM users WHERE username = ?\n        ', (username,))
    result = self.cursor.fetchone()
    return result