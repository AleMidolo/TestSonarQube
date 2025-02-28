def tzname_in_python2(namefunc):
    """
    Python 2 में यूनिकोड आउटपुट को बाइटस्ट्रिंग्स में बदलें।

    tzname() API ने Python 3 में बदलाव किया। पहले यह बाइट्स लौटाता था, 
    लेकिन इसे यूनिकोड स्ट्रिंग्स में बदल दिया गया।
    """
    def wrapper(*args, **kwargs):
        result = namefunc(*args, **kwargs)
        if isinstance(result, unicode):
            return result.encode('utf-8')
        return result
    return wrapper