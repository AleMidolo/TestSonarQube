def fetch_content_type(url: str) -> Optional[str]:
    """
    रिमोट यूआरएल का हेड प्राप्त करें ताकि कंटेंट टाइप निर्धारित किया जा सके।
    """
    import requests
    from typing import Optional
    
    try:
        # Send HEAD request to get headers without downloading content
        response = requests.head(url, allow_redirects=True, timeout=10)
        
        # Get content-type from headers
        content_type = response.headers.get('content-type')
        
        # Return content type if found, otherwise None
        return content_type if content_type else None
        
    except requests.RequestException:
        # Return None if request fails
        return None