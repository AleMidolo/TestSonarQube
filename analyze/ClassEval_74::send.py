def send(self, info):
    """
        पते और सामग्री को शामिल करने वाली जानकारी भेजें
        :param info: dict, जानकारी का डिक्शनरी जिसमें पता और सामग्री शामिल है
        :return: यदि सफलतापूर्वक भेजा गया, तो कुछ नहीं लौटाएं; अन्यथा, एक स्ट्रिंग लौटाएं जो एक त्रुटि संदेश को इंगित करती है
        >>> server.send({"addr":66,"content":"ABC"})
        self.send_struct = {"addr":66,"content":"ABC"}
        """
    if not isinstance(info, dict) or 'addr' not in info or 'content' not in info:
        return 'Invalid info format'
    self.send_struct = {'addr': info['addr'], 'content': info['content']}