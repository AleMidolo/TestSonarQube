def insert_user(self, username, password):
        """
        将新用户插入到 "users" 表中。
        :param username: str, 用户名。
        :param password: str, 用户的密码。
        :return: None
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        """
        self.cursor.execute('''
                INSERT INTO users (username, password) VALUES (?, ?)
            ''', (username, password))
        self.connection.commit()