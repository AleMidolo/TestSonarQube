def delete_user_by_username(self, username):
        """
        उपयोगकर्ता नाम द्वारा "users" तालिका से एक उपयोगकर्ता को हटाता है।
        :param username: str, हटाने के लिए उपयोगकर्ता का उपयोगकर्ता नाम।
        :return: None
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> user_db.delete_user_by_username('user1')
        """
        self.cursor.execute('''
                DELETE FROM users WHERE username = ?
            ''', (username,))
        self.connection.commit()