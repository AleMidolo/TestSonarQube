def insert_user(self, username, password):
    """
        Inserts a new user into the "users" table.
        :param username: str, the username of the user.
        :param password: str, the password of the user.
        :return: None
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        """
    self.cursor.execute('\n                INSERT INTO users (username, password) VALUES (?, ?)\n            ', (username, password))
    self.connection.commit()