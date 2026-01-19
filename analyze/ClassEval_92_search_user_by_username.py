def search_user_by_username(self, username):
    """
        "users" तालिका में उपयोगकर्ताओं को उपयोगकर्ता नाम द्वारा खोजता है।
        :param username: str, उस उपयोगकर्ता का उपयोगकर्ता नाम जिसे खोजा जाना है।
        :return: ट्यूपल की सूची, "users" तालिका से वे पंक्तियाँ जो खोज मानदंड से मेल खाती हैं।
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> result = user_db.search_user_by_username('user1')
        len(result) = 1
        """
    self.cursor.execute('\n            SELECT * FROM users WHERE username = ?\n        ', (username,))
    return self.cursor.fetchall()