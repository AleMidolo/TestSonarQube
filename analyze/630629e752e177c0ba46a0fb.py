def send_document(url, data, timeout=10, method="post", *args, **kwargs):
    import requests
    from requests.exceptions import RequestException

    try:
        # Convert method to lowercase
        method = method.lower()
        
        # Select HTTP method
        if method == "post":
            response = requests.post(url, data=data, timeout=timeout, *args, **kwargs)
        elif method == "put":
            response = requests.put(url, data=data, timeout=timeout, *args, **kwargs)
        elif method == "patch":
            response = requests.patch(url, data=data, timeout=timeout, *args, **kwargs)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        # Force raise for bad status codes
        response.raise_for_status()
        
        return response.status_code, None

    except RequestException as e:
        # Handle requests library exceptions
        if hasattr(e.response, 'status_code'):
            return e.response.status_code, e
        return None, e
        
    except Exception as e:
        # Handle any other exceptions
        return None, e