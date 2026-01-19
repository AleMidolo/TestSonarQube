def get_messages(self, username):
    """
        Ottieni tutti i messaggi di un utente dalla Chat.
        :param username: Il nome dell'utente, str.
        :return: Una lista di messaggi, ogni messaggio è un dizionario con le chiavi 'sender', 'receiver', 'message', 'timestamp'.
        >>> chat = Chat()
        >>> chat.users = {'John': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Ciao', 'timestamp': '2023-01-01 00:00:00'}]}
        >>> chat.get_messages('John')
        [{'sender': 'John', 'receiver': 'Mary', 'message': 'Ciao', 'timestamp': '2023-01-01 00:00:00'}]
        >>> chat.get_messages('Mary')
        []
        """
    if username in self.users:
        return self.users[username]
    return []