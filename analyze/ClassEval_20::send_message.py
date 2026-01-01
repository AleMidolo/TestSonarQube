def send_message(self, sender, receiver, message):
    """
        एक उपयोगकर्ता से दूसरे उपयोगकर्ता को संदेश भेजें।
        :param sender: प्रेषक का नाम, str.
        :param receiver: प्राप्तकर्ता का नाम, str.
        :param message: संदेश, str.
        :return: यदि प्रेषक या प्राप्तकर्ता चैट में नहीं है, तो False लौटाता है, अन्यथा, True लौटाता है।
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
    message_data = {'sender': sender, 'receiver': receiver, 'message': message, 'timestamp': timestamp}
    self.users[sender].append(message_data)
    self.users[receiver].append(message_data)
    return True