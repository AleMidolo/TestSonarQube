def validate_user_login(self, username, password):
    """
    Determine whether the user can log in, that is, the user is in the database and the password is correct
    :param username:str, the username of the user to validate.
    :param password:str, the password of the user to validate.
    :return:bool, representing whether the user can log in correctly
    >>> user_db = UserLoginDB("user_database.db")
    >>> user_db.create_table()
    >>> user_db.insert_user('user1', 'pass1')
    >>> user_db.validate_user_login('user1', 'pass1')
    True
    """
    cursor = self.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    return result is not None