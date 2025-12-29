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
        auth_header = request.get('headers', {}).get('Authorization', {})
        if isinstance(auth_header, dict) and 'user' in auth_header:
            return {'user': auth_header['user']}
        elif isinstance(auth_header, str):
            import json
            import base64
            parts = auth_header.split('.')
            if len(parts) == 3:
                payload = parts[1]
                payload += '=' * (4 - len(payload) % 4)
                decoded_payload = base64.b64decode(payload).decode('utf-8')
                user_data = json.loads(decoded_payload)
                if 'user' in user_data:
                    return {'user': user_data['user']}
    except Exception as e:
        logging.debug(f'Failed to parse JWT: {e}')
    return None