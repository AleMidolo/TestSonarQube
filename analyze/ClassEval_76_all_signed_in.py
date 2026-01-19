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
    if not hasattr(self, 'users') or not self.users:
        return True
    
    if not hasattr(self, 'signed_in_users'):
        return False
    
    return len(self.signed_in_users) == len(self.users)