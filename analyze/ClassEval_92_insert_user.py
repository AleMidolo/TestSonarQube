def insert_user(self, username, password):
    """
        Inserisce un nuovo utente nella tabella "users".
        :param username: str, il nome utente dell'utente.
        :param password: str, la password dell'utente.
        :return: None
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        """
    try:
        self.cursor.execute('\n                INSERT INTO users (username, password) VALUES (?, ?)\n            ', (username, password))
        self.connection.commit()
    except sqlite3.IntegrityError:
        pass