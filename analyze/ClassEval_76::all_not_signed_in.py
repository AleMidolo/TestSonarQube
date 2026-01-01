def all_not_signed_in(self):
    """
        获取未登录的用户名列表。
        :return: list[str]，未登录的用户名列表。
        >>> signInSystem = SignInSystem()
        >>> signInSystem.add_user("a")
        True
        >>> signInSystem.add_user("b")
        True
        >>> signInSystem.all_not_signed_in()
        ['a', 'b']
        """
    return [username for username, signed_in in self.users.items() if not signed_in]