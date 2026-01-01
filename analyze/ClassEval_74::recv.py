def recv(self, info):
    """
        पते और सामग्री को शामिल करने वाली जानकारी प्राप्त करें। यदि पता व्हाइटलिस्ट पर है, तो सामग्री प्राप्त करें; अन्यथा, इसे प्राप्त न करें
        :param info: dict, जानकारी शब्दकोश जिसमें पता और सामग्री शामिल है
        :return: यदि सफलतापूर्वक प्राप्त किया गया, तो जानकारी की सामग्री लौटाएं; अन्यथा, False लौटाएं
        >>> server.recv({"addr":88,"content":"abc"})
        abc
        """
    if not isinstance(info, dict) or 'addr' not in info or 'content' not in info:
        return False
    addr = info['addr']
    content = info['content']
    if addr in self.white_list:
        self.receive_struct = {'addr': addr, 'content': content}
        return content
    else:
        return False