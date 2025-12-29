def send_message(self, sender, receiver, message):
    """
        Invia un messaggio da un utente a un altro utente.
        :param sender: Il nome del mittente, str.
        :param receiver: Il nome del destinatario, str.
        :param message: Il messaggio, str.
        :return: Se il mittente o il destinatario non sono nel Chat, restituisce False, altrimenti restituisce True.
        >>> chat = Chat()
        >>> chat.users = {'John': [], 'Mary': []}
        >>> chat.send_message('John', 'Mary', 'Ciao')
        True
        >>> chat.send_message('John', 'Tom', 'Ciao')
        False

        """
    if sender not in self.users or receiver not in self.users:
        return False
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message_dict = {'sender': sender, 'receiver': receiver, 'message': message, 'timestamp': timestamp}
    self.users[sender].append(message_dict)
    self.users[receiver].append(message_dict)
    return True