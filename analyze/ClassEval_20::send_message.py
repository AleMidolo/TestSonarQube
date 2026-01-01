def send_message(self, sender, receiver, message):
    """
        Envía un mensaje de un usuario a otro usuario.
        :param sender: El nombre del remitente, str.
        :param receiver: El nombre del receptor, str.
        :param message: El mensaje, str.
        :return: Si el remitente o el receptor no están en el Chat, devuelve False, de lo contrario, devuelve True.
        >>> chat = Chat()
        >>> chat.users = {'John': [], 'Mary': []}
        >>> chat.send_message('John', 'Mary', 'Hola')
        True
        >>> chat.send_message('John', 'Tom', 'Hola')
        False

        """
    if sender not in self.users or receiver not in self.users:
        return False
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message_dict = {'sender': sender, 'receiver': receiver, 'message': message, 'timestamp': timestamp}
    self.users[sender].append(message_dict)
    self.users[receiver].append(message_dict)
    return True