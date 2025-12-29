def get_jwt_user(self, request):
    """
        Ottieni le informazioni dell'utente dal token JWT nella richiesta.
        :param request: dict, i dettagli della richiesta in arrivo
        :return: dict o None, le informazioni dell'utente se il token è valido, None altrimenti
        >>> filter = AccessGatewayFilter()
        >>> filter.get_jwt_user({'headers': {'Authorization': {'user': {'name': 'user1'}, 'jwt': 'user1'+str(datetime.date.today())}}})
        {'user': {'name': 'user1'}}
        """
    try:
        auth_header = request.get('headers', {}).get('Authorization', {})
        if 'jwt' in auth_header and 'user' in auth_header:
            return {'user': auth_header['user']}
    except:
        pass
    return None