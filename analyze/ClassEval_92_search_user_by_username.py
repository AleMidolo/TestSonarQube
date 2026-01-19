def search_user_by_username(self, username):
    """
        Searches for users in the "users" table by username.
        :param username: str, the username of the user to search for.
        :return: tuple or None, the row from the "users" table that matches the search criteria, or None if not found.
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> result = user_db.search_user_by_username('user1')
        len(result) = 1
        """
    self.cursor.execute('\n            SELECT * FROM users WHERE username = ?\n        ', (username,))
    result = self.cursor.fetchone()
    return result