def validate_user_login(self, username, password):
    """
    判断用户是否可以登录，即用户是否在数据库中且密码是否正确
    :param username:str, 要验证的用户的用户名。
    :param password:str, 要验证的用户的密码。
    :return:bool, 表示用户是否可以正确登录
    >>> user_db = UserLoginDB("user_database.db")
    >>> user_db.create_table()
    >>> user_db.insert_user('user1', 'pass1')
    >>> user_db.validate_user_login('user1', 'pass1')
    True
    """
    self.cursor.execute('''
            SELECT * FROM users WHERE username = ? AND password = ?
        ''', (username, password))
    user = self.cursor.fetchone()
    return user is not None