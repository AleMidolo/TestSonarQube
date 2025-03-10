from functools import wraps

def unit_of_work(metadata=None, timeout=None):
    """
    यह फ़ंक्शन ट्रांज़ेक्शन फ़ंक्शन्स के लिए एक डेकोरेटर है, जो यह नियंत्रित करने की अतिरिक्त सुविधा प्रदान करता है कि ट्रांज़ेक्शन कैसे निष्पादित किया जाए।

    :param metadata: मेटाडेटा के साथ एक डिक्शनरी।
    :type metadata: dict
    :param timeout: ट्रांज़ेक्शन का टाइमआउट (सेकंड में)।
    :type timeout: float या None
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # यहां ट्रांज़ेक्शन के लिए मेटाडेटा और टाइमआउट को सेट करें
            if metadata is not None:
                kwargs['metadata'] = metadata
            if timeout is not None:
                kwargs['timeout'] = timeout
            return func(*args, **kwargs)
        return wrapper
    return decorator