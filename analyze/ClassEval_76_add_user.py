def add_user(self, username):
    """
        यदि उपयोगकर्ता self.users में नहीं है तो साइन-इन सिस्टम में एक उपयोगकर्ता जोड़ें।
        और प्रारंभिक स्थिति False है।
        :param username: str, जो उपयोगकर्ता नाम जोड़ा जाना है।
        :return: bool, यदि उपयोगकर्ता सफलतापूर्वक जोड़ा गया है तो True, यदि उपयोगकर्ता पहले से मौजूद है तो False।
        >>> signInSystem.add_user("mike")
        True
        >>> signInSystem.add_user("mike")
        False
        """
    if username in self.users:
        return False
    else:
        self.users[username] = False
        return True