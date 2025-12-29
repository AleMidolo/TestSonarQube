def validate_user_login(self, username, password):
    """
        निर्धारित करें कि क्या उपयोगकर्ता लॉग इन कर सकता है, अर्थात्, उपयोगकर्ता डेटाबेस में है और पासवर्ड सही है
        :param username:str, उपयोगकर्ता का उपयोगकर्ता नाम जिसे मान्य करना है।
        :param password:str, उपयोगकर्ता का पासवर्ड जिसे मान्य करना है।
        :return:bool, यह दर्शाता है कि क्या उपयोगकर्ता सही तरीके से लॉग इन कर सकता है
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.insert_user('user1', 'pass1')
        >>> user_db.validate_user_login('user1', 'pass1')
        True
        """
    user = self.search_user_by_username(username)
    if user is None:
        return False
    stored_password = user[2]
    return stored_password == password