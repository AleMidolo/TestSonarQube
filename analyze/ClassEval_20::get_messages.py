def get_messages(self, username):
    """
        获取用户在聊天中的所有消息。
        :param username: 用户名，str。
        :return: 消息列表，每条消息是一个字典，包含键 'sender', 'receiver', 'message', 'timestamp'。
        >>> chat = Chat()
        >>> chat.users = {'John': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]}
        >>> chat.get_messages('John')
        [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]
        >>> chat.get_messages('Mary')
        []
        """
    if username not in self.users:
        return []
    return self.users[username]