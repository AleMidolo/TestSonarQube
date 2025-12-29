@staticmethod
def remove(states, stat):
    """
        अभी की स्थिति से बताया गया स्टेटस हटाएँ, और चेक करें कि पैरामीटर लीगल हैं या नहीं।

        :param states: अभी की स्थिति, int
        :param stat: बताया गया स्टेटस, int
        :return: बताया गया स्टेटस हटाने के बाद का स्टेटस, int

        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.remove(6, 2)
        4
        """
    BitStatusUtil.check([states, stat])
    return states & ~stat