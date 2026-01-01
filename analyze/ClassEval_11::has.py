@staticmethod
def has(states, stat):
    """
        चेक करता है कि अभी के स्टेटस में बताया गया स्टेटस है या नहीं, और चेक करता है कि पैरामीटर वैलिड हैं या नहीं।

        :param states: अभी का स्टेटस, int
        :param stat: बताया गया स्टेटस, int
        :return: अगर अभी के स्टेटस में बताया गया स्टेटस है तो True, नहीं तो False, bool

        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.has(6, 2)
        True
        """
    BitStatusUtil.check([states, stat])
    return states & stat == stat