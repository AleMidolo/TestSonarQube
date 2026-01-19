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
    
    headers = request['headers']
    if 'Authorization' not in headers:
        return None
    
    auth_data = headers['Authorization']
    if not isinstance(auth_data, dict):
        return None
    
    # Verifica che il JWT sia valido (contiene la data odierna)
    if 'jwt' in auth_data and 'user' in auth_data:
        jwt_token = auth_data['jwt']
        # Verifica che il token contenga la data odierna
        if str(datetime.date.today()) in jwt_token:
            return {'user': auth_data['user']}
    
    return None