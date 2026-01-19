def get_jwt_user(self, request):
    """
    Ottieni le informazioni dell'utente dal token JWT nella richiesta.
    :param request: dict, i dettagli della richiesta in arrivo
    :return: dict o None, le informazioni dell'utente se il token è valido, None altrimenti
    >>> filter = AccessGatewayFilter()
    >>> filter.get_jwt_user({'headers': {'Authorization': {'user': {'name': 'user1'}, 'jwt': 'user1'+str(datetime.date.today())}}})
    {'user': {'name': 'user1'}

    """
    if not request or 'headers' not in request:
        return None
    
    headers = request.get('headers', {})
    authorization = headers.get('Authorization')
    
    if not authorization:
        return None
    
    if isinstance(authorization, dict) and 'user' in authorization:
        return {'user': authorization['user']}
    
    return None