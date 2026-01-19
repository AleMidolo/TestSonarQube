import datetime

def get_jwt_user(self, request):
    """
    अनुरोध में JWT टोकन से उपयोगकर्ता की जानकारी प्राप्त करें।
    :param request: dict, आने वाले अनुरोध का विवरण
    :return: dict या None, यदि टोकन मान्य है तो उपयोगकर्ता की जानकारी, अन्यथा None
    >>> filter = AccessGatewayFilter()
    >>> filter.get_jwt_user({'headers': {'Authorization': {'user': {'name': 'user1'}, 'jwt': 'user1'+str(datetime.date.today())}}})
    {'user': {'name': 'user1'}
    """
    try:
        # अनुरोध से headers प्राप्त करें
        headers = request.get('headers', {})
        
        # Authorization header प्राप्त करें
        authorization = headers.get('Authorization', {})
        
        # यदि authorization dict नहीं है, तो None लौटाएं
        if not isinstance(authorization, dict):
            return None
        
        # JWT टोकन और उपयोगकर्ता जानकारी प्राप्त करें
        jwt_token = authorization.get('jwt', '')
        user_info = authorization.get('user', {})
        
        # यदि user_info में name है, तो JWT टोकन को validate करें
        if user_info and 'name' in user_info:
            username = user_info['name']
            expected_token = username + str(datetime.date.today())
            
            # JWT टोकन की जांच करें
            if jwt_token == expected_token:
                return {'user': user_info}
        
        return None
    except Exception:
        return None