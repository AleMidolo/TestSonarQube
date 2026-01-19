def send(self, info):
    """
    पते और सामग्री को शामिल करने वाली जानकारी भेजें
    :param info: dict, जानकारी का डिक्शनरी जिसमें पता और सामग्री शामिल है
    :return: यदि सफलतापूर्वक भेजा गया, तो कुछ नहीं लौटाएं; अन्यथा, एक स्ट्रिंग लौटाएं जो एक त्रुटि संदेश को इंगित करती है
    >>> server.send({"addr":66,"content":"ABC"})
    self.send_struct = {"addr":66,"content":"ABC"}
    """
    try:
        if not isinstance(info, dict):
            return "Error: info must be a dictionary"
        
        if "addr" not in info or "content" not in info:
            return "Error: info must contain 'addr' and 'content' keys"
        
        self.send_struct = info
        return None
    except Exception as e:
        return f"Error: {str(e)}"