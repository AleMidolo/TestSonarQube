@staticmethod
def check(args):
    """
    जांचें कि पैरामीटर वैध हैं या नहीं, args को 0 से बड़ा या उसके बराबर होना चाहिए और यह सम होना चाहिए, यदि नहीं, तो ValueError उठाएं।
    :param args: जांचे जाने वाले पैरामीटर, सूची।
    :return: कुछ नहीं।
    >>> bit_status_util = BitStatusUtil()
    >>> bit_status_util.check([2,3,4])
    Traceback (most recent call last):
    ...
    ValueError: 3 सम नहीं है
    """
    for arg in args:
        if arg < 0:
            raise ValueError(f"{arg} 0 से बड़ा या उसके बराबर नहीं है")
        if arg % 2 != 0:
            raise ValueError(f"{arg} सम नहीं है")