def get_messages(self, username):
    """
    एक उपयोगकर्ता के सभी संदेशों को चैट से प्राप्त करें।
    :param username: उपयोगकर्ता का नाम, str.
    :return: संदेशों की एक सूची, प्रत्येक संदेश एक शब्दकोश है जिसमें 'sender', 'receiver', 'message', 'timestamp' कुंजी हैं।
    >>> chat = Chat()
    >>> chat.users = {'John': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]}
    >>> chat.get_messages('John')
    [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]
    >>> chat.get_messages('Mary')
    []

    """
    if username in self.users:
        return self.users[username]
    else:
        return []