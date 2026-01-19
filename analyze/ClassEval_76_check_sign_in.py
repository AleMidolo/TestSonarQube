def check_sign_in(self, username):
    """
        जांचें कि क्या एक उपयोगकर्ता साइन इन है।
        :param username: str, जांचने के लिए उपयोगकर्ता नाम।
        :return: bool, True यदि उपयोगकर्ता साइन इन है, False यदि उपयोगकर्ता मौजूद नहीं है या साइन इन नहीं है।
        >>> signInSystem.check_sign_in("jack")
        False
        >>> signInSystem.add_user("jack")
        >>> signInSystem.check_sign_in("jack")
        >>> signInSystem.sign_in("jack")
        >>> signInSystem.check_sign_in("jack")
        True
        """
    if username not in self.users or not self.users[username]:
        return False
    return True