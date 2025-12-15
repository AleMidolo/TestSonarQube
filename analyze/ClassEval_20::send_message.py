def send_message(self, sender, receiver, message):
        """
        Send a message from a user to another user.
        :param sender: The sender's name, str.
        :param receiver: The receiver's name, str.
        :param message: The message, str.
        :return: If the sender or the receiver is not in the Chat, returns False, otherwise, returns True.
        >>> chat = Chat()
        >>> chat.users = {'John': [], 'Mary': []}
        >>> chat.send_message('John', 'Mary', 'Hello')
        True
        >>> chat.send_message('John', 'Tom', 'Hello')
        False

        """
        if sender not in self.users or receiver not in self.users:
            return False
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.users[sender].append({'sender': sender, 'receiver': receiver, 'message': message, 'timestamp': timestamp})
        self.users[receiver].append({'sender': sender, 'receiver': receiver, 'message': message, 'timestamp': timestamp})
        return True