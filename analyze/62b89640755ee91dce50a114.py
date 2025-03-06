def tzname_in_python2(namefunc):
    """
    Python 2 में यूनिकोड आउटपुट को बाइटस्ट्रिंग्स में बदलें।

    tzname() API ने Python 3 में बदलाव किया। पहले यह बाइट्स लौटाता था, 
    लेकिन इसे यूनिकोड स्ट्रिंग्स में बदल दिया गया।
    """
    def wrapper(*args, **kwargs):
        result = namefunc(*args, **kwargs)
        if isinstance(result, str):
            return result.encode('utf-8')
        elif isinstance(result, tuple):
            return tuple(x.encode('utf-8') if isinstance(x, str) else x for x in result)
        return result
    return wrapper