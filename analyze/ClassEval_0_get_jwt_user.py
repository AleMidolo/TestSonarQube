def get_jwt_user(self, request):
    """
    Ottieni le informazioni dell'utente dal token JWT nella richiesta.
    :param request: dict, i dettagli della richiesta in arrivo
    :return: dict o None, le informazioni dell'utente se il token è valido, None altrimenti
    >>> filter = AccessGatewayFilter()
    >>> filter.get_jwt_user({'headers': {'Authorization': {'user': {'name': 'user1'}, 'jwt': 'user1'+str(datetime.date.today())}}})
    {'user': {'name': 'user1'}

    """
    try:
        # Verifica che la richiesta contenga headers
        if not request or 'headers' not in request:
            return None
        
        headers = request['headers']
        
        # Verifica che ci sia l'header Authorization
        if 'Authorization' not in headers:
            return None
        
        auth_data = headers['Authorization']
        
        # Verifica che Authorization contenga i dati dell'utente
        if not isinstance(auth_data, dict):
            return None
        
        # Verifica che ci sia il campo 'user'
        if 'user' not in auth_data:
            return None
        
        # Restituisce le informazioni dell'utente
        return {'user': auth_data['user']}
    
    except (KeyError, TypeError, AttributeError):
        return None