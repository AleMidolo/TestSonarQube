from datetime import datetime

class Chat:
    def __init__(self):
        self.users = {}

    def add_user(self, username):
        if self._user_exists(username):
            return False
        self.users[username] = []
        return True

    def remove_user(self, username):
        if self._user_exists(username):
            del self.users[username]
            return True
        return False

    def send_message(self, sender, receiver, message):
        if not self._users_exist(sender, receiver):
            return False

        message_info = self._create_message_info(sender, receiver, message)
        self._store_message(sender, message_info)
        self._store_message(receiver, message_info)
        return True

    def get_messages(self, username):
        if not self._user_exists(username):
            return []
        return self.users[username]

    def _user_exists(self, username):
        return username in self.users

    def _users_exist(self, sender, receiver):
        return self._user_exists(sender) and self._user_exists(receiver)

    def _create_message_info(self, sender, receiver, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            'sender': sender,
            'receiver': receiver,
            'message': message,
            'timestamp': timestamp
        }

    def _store_message(self, username, message_info):
        self.users[username].append(message_info)