def sign_in(self, username):
    """
        यदि उपयोगकर्ता self.users में है तो उपयोगकर्ता को साइन इन करें और स्थिति को True में बदलें।
        :param username: str, साइन इन करने के लिए उपयोगकर्ता नाम।
        :return: bool, यदि उपयोगकर्ता सफलतापूर्वक साइन इन होता है तो True, यदि उपयोगकर्ता मौजूद नहीं है तो False।
        >>> signInSystem.sign_in("mike")
        True
        >>> signInSystem.sign_in("mik")
        False
        """
    if username in self.users:
        self.users[username] = True
        return True
    return False