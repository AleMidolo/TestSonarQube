from datetime import datetime

class Chat: 
    def __init__(self):
        """
        Initialize the Chat with an attribute users, which is an empty dictionary.
        """
        self.users = {}

    def remove_user(self, username):
        """
        Remove a user from the Chat.
        :param username: The user's name, str.
        :return: If the user is already in the Chat, returns True, otherwise, returns False.
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
        else:
            return False
    
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

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message_info = {
            'sender': sender,
            'receiver': receiver,
            'message': message,
            'timestamp': timestamp
        }
        self.users[sender].append(message_info)
        self.users[receiver].append(message_info)
        return True
    
    def get_messages(self, username):
        """
        Get all the messages of a user from the Chat.
        :param username: The user's name, str.
        :return: A list of messages, each message is a dictionary with keys 'sender', 'receiver', 'message', 'timestamp'.
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
    
    def add_user(self, username):
        """
        चैट में एक नया उपयोगकर्ता जोड़ें।
        :param username: उपयोगकर्ता का नाम, str.
        :return: यदि उपयोगकर्ता पहले से चैट में है, तो False लौटाता है, अन्यथा, True लौटाता है।
        >>> chat = Chat()
        >>> chat.add_user('John')
        True
        >>> chat.users = {'John': []}
        >>> chat.add_user('John')
        False
        """
        if username in self.users:
            return False
        self.users[username] = []
        return True