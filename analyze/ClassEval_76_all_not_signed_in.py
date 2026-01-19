def all_not_signed_in(self):
    """
    उन उपयोगकर्ता नामों की सूची प्राप्त करें जो साइन इन नहीं हैं।
    :return: list[str], उन उपयोगकर्ता नामों की सूची जो साइन इन नहीं हैं।
    >>> signInSystem = SignInSystem()
    >>> signInSystem.add_user("a")
    True
    >>> signInSystem.add_user("b")
    True
    >>> signInSystem.all_not_signed_in()
    ['a', 'b']
    """
    return [user for user in self.users if user not in self.signed_in_users]