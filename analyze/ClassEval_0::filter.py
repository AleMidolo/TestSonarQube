def filter(self, request):
    """
        कुछ नियमों और शर्तों के आधार पर आने वाले अनुरोध को फ़िल्टर करें।
        :param request: dict, आने वाले अनुरोध का विवरण
        :return: bool, यदि अनुरोध की अनुमति है तो True, अन्यथा False
        >>> filter = AccessGatewayFilter()
        >>> filter.filter({'path': '/login', 'method': 'POST'})
        True
        """
    if self.is_start_with(request['path']):
        return True
    return False