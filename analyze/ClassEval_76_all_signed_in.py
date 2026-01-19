def all_signed_in(self):
    """
    Check if all users are signed in.
    :return: bool, True if all users are signed in, False otherwise.
    >>> signInSystem.add_user("jack")
    True
    >>> signInSystem.sign_in("jack")
    >>> signInSystem.all_signed_in()
    True
    """
    if not self.users:
        return True
    return all(user in self.signed_in_users for user in self.users)