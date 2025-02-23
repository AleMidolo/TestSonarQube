def send_document(url, data, timeout=10, method="post", *args, **kwargs):
    """
    Helper method to send a document via POST.

    Additional ``*args`` and ``**kwargs`` will be passed on to ``requests.post``.

    :arg url: Full url to send to, including protocol
    :arg data: Dictionary (will be form-encoded), bytes, or file-like object to send in the body
    :arg timeout: Seconds to wait for response (defaults to 10)
    :arg method: Method to use, defaults to post
    :returns: Tuple of status code (int or None) and error (exception class instance or None)
    """
    import requests

    try:
        if method.lower() == "post":
            response = requests.post(url, data=data, timeout=timeout, *args, **kwargs)
        else:
            raise ValueError("Unsupported method: {}".format(method))

        return response.status_code, None
    except Exception as e:
        return None, e