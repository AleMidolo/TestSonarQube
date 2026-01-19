def all_signed_in(self):
    """
    检查所有用户是否已登录。
    :return: bool，如果所有用户已登录则返回 True，否则返回 False。
    >>> signInSystem.add_user("jack")
    True
    >>> signInSystem.sign_in("jack")
    >>> signInSystem.all_signed_in()
    True
    """
    if not self.users:
        return True
    
    for user in self.users:
        if user not in self.signed_in_users:
            return False
    
    return True