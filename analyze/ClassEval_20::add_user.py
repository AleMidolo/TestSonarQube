def add_user(self, username):
    """
        चैट में एक नया उपयोगकर्ता जोड़ें।
        :param username: उपयोगकर्ता का नाम, str.
        :return: यदि उपयोगकर्ता पहले से चैट में है, तो False लौटाता है, अन्यथा, True लौटाता है।
        >>> chat = Chat()
        >>> chat.add_user('John')
        True
        self.users = {'John': []}
        >>> chat.add_user('John')
        False

        """
    if username in self.users:
        return False
    self.users[username] = []
    return True