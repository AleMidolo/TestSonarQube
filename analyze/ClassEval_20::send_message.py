def send_message(self, sender, receiver, message):
    """
        从一个用户发送消息到另一个用户。
        :param sender: 发送者的名字，str。
        :param receiver: 接收者的名字，str。
        :param message: 消息内容，str。
        :return: 如果发送者或接收者不在聊天中，返回 False；否则，返回 True。
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
    self.users[receiver].append({'sender': sender, 'receiver': receiver, 'message': message, 'timestamp': timestamp})
    return True