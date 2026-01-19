def all_signed_in(self):
    """
        सभी उपयोगकर्ताओं के साइन इन होने की जांच करें।
        :return: bool, यदि सभी उपयोगकर्ता साइन इन हैं तो True, अन्यथा False।
        >>> signInSystem.add_user("jack")
        True
        >>> signInSystem.sign_in("jack")
        >>> signInSystem.all_signed_in()
        True
        """
    if not self.users:
        return False
    for signed_in in self.users.values():
        if not signed_in:
            return False
    return True