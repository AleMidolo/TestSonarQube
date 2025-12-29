def delete_user_by_username(self, username):
    """
        根据用户名从“users”表中删除用户。
        :param username: str，要删除的用户的用户名。
        :return: None
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> user_db.delete_user_by_username('user1')
        """
    self.cursor.execute('\n            DELETE FROM users WHERE username = ?\n        ', (username,))
    self.connection.commit()