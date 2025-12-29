def remove_user(self, username):
    """
        चैट से एक उपयोगकर्ता को हटाएं।
        :param username: उपयोगकर्ता का नाम, str.
        :return: यदि उपयोगकर्ता पहले से चैट में है, तो True लौटाता है, अन्यथा, False लौटाता है।
        >>> chat = Chat()
        >>> chat.users = {'John': []}
        >>> chat.remove_user('John')
        True
        >>> chat.remove_user('John')
        False
        """
    if username in self.users:
        del self.users[username]
        return True
    return False