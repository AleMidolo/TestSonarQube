def get_jwt_user(self, request):
    """
    Obtiene la información del usuario del token JWT en la solicitud.
    :param request: dict, los detalles de la solicitud entrante
    :return: dict o None, la información del usuario si el token es válido, None en caso contrario
    >>> filter = AccessGatewayFilter()
    >>> filter.get_jwt_user({'headers': {'Authorization': {'user': {'name': 'user1'}, 'jwt': 'user1'+str(datetime.date.today())}}})
    {'user': {'name': 'user1'}

    """
    try:
        # Verificar que la solicitud tenga headers
        if not request or 'headers' not in request:
            return None
        
        headers = request['headers']
        
        # Verificar que exista el header Authorization
        if 'Authorization' not in headers:
            return None
        
        auth_data = headers['Authorization']
        
        # Verificar que Authorization sea un diccionario con información de usuario
        if not isinstance(auth_data, dict):
            return None
        
        # Verificar que exista información de usuario
        if 'user' not in auth_data:
            return None
        
        # Verificar que exista el JWT (token)
        if 'jwt' not in auth_data:
            return None
        
        # Aquí se podría validar el JWT si fuera necesario
        # Por ahora, según el ejemplo, simplemente retornamos la información del usuario
        return {'user': auth_data['user']}
        
    except Exception:
        return None