def send_document(url, data, timeout=10, method="post", *args, **kwargs):
    import requests
    
    status_code = None
    error = None
    
    try:
        # Prepare request method
        request_method = getattr(requests, method.lower())
        
        # Send request
        response = request_method(
            url,
            data=data,
            timeout=timeout,
            *args,
            **kwargs
        )
        
        # Get status code
        status_code = response.status_code
        
        # Raise for bad status codes
        response.raise_for_status()
            
    except requests.exceptions.RequestException as e:
        error = e
        if status_code is None and hasattr(e.response, 'status_code'):
            status_code = e.response.status_code
            
    except Exception as e:
        error = e
        
    return status_code, error