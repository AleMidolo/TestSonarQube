def search_user_by_username(self, username):
    """
        Searches for users in the "users" table by username.
        :param username: str, the username of the user to search for.
        :return: tuple or None, the row from the "users" table that matches the search criteria.
        """
    self.cursor.execute('\n            SELECT username, password FROM users WHERE username = ?\n        ', (username,))
    result = self.cursor.fetchone()
    return result