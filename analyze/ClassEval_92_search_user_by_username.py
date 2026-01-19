def search_user_by_username(self, username):
    """
        Cerca utenti nella tabella "users" per nome utente.
        :param username: str, il nome utente dell'utente da cercare.
        :return: lista di tuple, le righe dalla tabella "users" che corrispondono ai criteri di ricerca.
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> result = user_db.search_user_by_username('user1')
        len(result) = 1
        """
    self.cursor.execute('\n            SELECT username, password FROM users WHERE username = ?\n        ', (username,))
    result = self.cursor.fetchone()
    return result