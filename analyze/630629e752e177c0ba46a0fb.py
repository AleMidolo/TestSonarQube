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
        # Get the appropriate request method
        request_method = getattr(requests, method.lower())
        
        # Make the request
        response = request_method(
            url,
            data=data,
            timeout=timeout,
            *args,
            **kwargs
        )
        
        # Return status code and None for error
        return response.status_code, None
        
    except requests.exceptions.RequestException as e:
        # Return None for status code and the exception for error
        return None, e
    except Exception as e:
        # Handle any other unexpected errors
        return None, e