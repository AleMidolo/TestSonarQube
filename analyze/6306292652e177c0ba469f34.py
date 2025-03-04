def fetch_content_type(url: str) -> Optional[str]:
    """
    Fetch the HEAD of the remote url to determine the content type.
    """
    import requests
    from typing import Optional
    
    try:
        response = requests.head(url, allow_redirects=True)
        return response.headers.get('content-type')
    except requests.RequestException:
        return None