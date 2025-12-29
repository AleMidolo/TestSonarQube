def insert_user(self, username, password):
    """
        "users" तालिका में एक नया उपयोगकर्ता डालता है।
        :param username: str, उपयोगकर्ता का उपयोगकर्ता नाम।
        :param password: str, उपयोगकर्ता का पासवर्ड।
        :return: None
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        """
    self.cursor.execute('\n            INSERT INTO users (username, password) VALUES (?, ?)\n        ', (username, password))
    self.connection.commit()