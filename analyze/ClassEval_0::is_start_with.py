def is_start_with(self, request_uri):
    """
        जांचें कि क्या अनुरोध URI कुछ उपसर्गों से शुरू होता है।
        वर्तमान में, जांचे जा रहे उपसर्ग "/api" और "/login" हैं।
        :param request_uri: str, अनुरोध का URI
        :return: bool, यदि URI कुछ उपसर्गों से शुरू होता है तो True, अन्यथा False
        >>> filter = AccessGatewayFilter()
        >>> filter.is_start_with('/api/data')
        True

        """
    prefixes = ['/api', '/login']
    for prefix in prefixes:
        if request_uri.startswith(prefix):
            return True
    return False