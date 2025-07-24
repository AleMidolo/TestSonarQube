class SignInSystem:
    def __init__(self):
        self.users = {}

    def add_user(self, username):
        if self._is_user_exists(username):
            return False
        self.users[username] = False
        return True

    def sign_in(self, username):
        if not self._is_user_exists(username):
            return False
        self.users[username] = True
        return True

    def check_sign_in(self, username):
        if not self._is_user_exists(username):
            return False
        return self.users[username]

    def all_signed_in(self):
        return all(self.users.values())

    def all_not_signed_in(self):
        return [username for username, signed_in in self.users.items() if not signed_in]

    def _is_user_exists(self, username):
        return username in self.users