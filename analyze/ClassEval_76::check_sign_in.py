def check_sign_in(self, username):
    """
        检查用户是否已登录。
        :param username: str，要检查的用户名。
        :return: bool，如果用户已登录则返回True，如果用户不存在或未登录则返回False。
        >>> signInSystem.check_sign_in("jack")
        False
        >>> signInSystem.add_user("jack")
        >>> signInSystem.check_sign_in("jack")
        >>> signInSystem.sign_in("jack")
        >>> signInSystem.check_sign_in("jack")
        True
        """
    if username not in self.users:
        return False
    return self.users[username]