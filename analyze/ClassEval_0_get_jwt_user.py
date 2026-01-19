def get_jwt_user(self, request):
    """
        अनुरोध में JWT टोकन से उपयोगकर्ता की जानकारी प्राप्त करें।
        :param request: dict, आने वाले अनुरोध का विवरण
        :return: dict या None, यदि टोकन मान्य है तो उपयोगकर्ता की जानकारी, अन्यथा None
        >>> filter = AccessGatewayFilter()
        >>> filter.get_jwt_user({'headers': {'Authorization': {'user': {'name': 'user1'}, 'jwt': 'user1'+str(datetime.date.today())}}})
        {'user': {'name': 'user1'}}
        """
    try:
        if 'headers' in request and 'Authorization' in request['headers']:
            auth_data = request['headers']['Authorization']
            if isinstance(auth_data, dict) and 'user' in auth_data:
                return {'user': auth_data['user']}
    except:
        return None
    return None