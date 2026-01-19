def get_jwt_user(self, request):
    """
    Ottieni le informazioni dell'utente dal token JWT nella richiesta.
    :param request: dict, i dettagli della richiesta in arrivo
    :return: dict o None, le informazioni dell'utente se il token è valido, None altrimenti
    >>> filter = AccessGatewayFilter()
    >>> filter.get_jwt_user({'headers': {'Authorization': {'user': {'name': 'user1'}, 'jwt': 'user1'+str(datetime.date.today())}}})
    {'user': {'name': 'user1'}

    """
    import datetime
    
    if not request or 'headers' not in request:
        return None
    
    headers = request.get('headers', {})
    authorization = headers.get('Authorization')
    
    if not authorization:
        return None
    
    # Verifica se l'authorization contiene le informazioni necessarie
    if not isinstance(authorization, dict):
        return None
    
    jwt_token = authorization.get('jwt')
    user_info = authorization.get('user')
    
    if not jwt_token or not user_info:
        return None
    
    # Verifica che il token JWT sia valido (contiene il nome utente e la data odierna)
    if 'name' in user_info:
        expected_token = user_info['name'] + str(datetime.date.today())
        if jwt_token == expected_token:
            return {'user': user_info}
    
    return None