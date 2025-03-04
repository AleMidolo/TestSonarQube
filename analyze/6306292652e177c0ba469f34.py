def fetch_content_type(url: str) -> Optional[str]:
    """
    रिमोट यूआरएल का हेड प्राप्त करें ताकि कंटेंट टाइप निर्धारित किया जा सके।
    """
    try:
        import requests
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.headers.get('content-type')
    except:
        return None