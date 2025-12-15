def remove_user(self, username):
        """
        Rimuovi un utente dalla Chat.
        :param username: Il nome dell'utente, str.
        :return: Se l'utente è già nella Chat, restituisce True, altrimenti restituisce False.
        >>> chat = Chat()
        >>> chat.users = {'John': []}
        >>> chat.remove_user('John')
        True
        >>> chat.remove_user('John')
        False

        """
        if username in self.users:
            del self.users[username]
            return True
        return False