def show(self, type):
    """
    निर्दिष्ट प्रकार की संरचना लौटाता है
    :param type: स्ट्रिंग, वह संरचना का प्रकार जो लौटाया जाएगा, जो 'send' या 'receive' हो सकता है
    :return: यदि type 'send' या 'receive' के बराबर है, तो संबंधित संरचना लौटाएं; अन्यथा, False लौटाएं
    >>> server.recv({"addr":88,"content":"abc"})
    >>> server.send({"addr":66,"content":"ABC"})
    >>> server.show("send")
    {"addr":66,"content":"ABC"}
    """
    if type == "send":
        return self._send_structure
    elif type == "receive":
        return self._receive_structure
    else:
        return False