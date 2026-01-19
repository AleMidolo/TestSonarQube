def recv(self, info):
    """
    पते और सामग्री को शामिल करने वाली जानकारी प्राप्त करें। यदि पता व्हाइटलिस्ट पर है, तो सामग्री प्राप्त करें; अन्यथा, इसे प्राप्त न करें
    :param info: dict, जानकारी शब्दकोश जिसमें पता और सामग्री शामिल है
    :return: यदि सफलतापूर्वक प्राप्त किया गया, तो जानकारी की सामग्री लौटाएं; अन्यथा, False लौटाएं
    >>> server.recv({"addr":88,"content":"abc"})
    abc
    """
    if "addr" in info and "content" in info:
        if hasattr(self, 'whitelist') and info["addr"] in self.whitelist:
            return info["content"]
    return False