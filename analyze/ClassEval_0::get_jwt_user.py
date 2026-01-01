def get_jwt_user(self, request):
    """
        Obtiene la información del usuario del token JWT en la solicitud.
        :param request: dict, los detalles de la solicitud entrante
        :return: dict o None, la información del usuario si el token es válido, None en caso contrario
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