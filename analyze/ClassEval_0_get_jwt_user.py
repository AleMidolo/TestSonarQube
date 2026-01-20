def get_jwt_user(self, request):
    """
    Obtiene la información del usuario del token JWT en la solicitud.
    :param request: dict, los detalles de la solicitud entrante
    :return: dict o None, la información del usuario si el token es válido, None en caso contrario
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
    
    # Si Authorization es un diccionario con información de usuario y JWT
    if isinstance(authorization, dict):
        jwt_token = authorization.get('jwt')
        user_info = authorization.get('user')
        
        if jwt_token and user_info:
            # Validar que el JWT contiene la fecha de hoy
            # Según el ejemplo, el JWT debe contener el nombre de usuario + fecha de hoy
            expected_date = str(datetime.date.today())
            
            # Verificar que el token es válido (contiene la fecha de hoy)
            if expected_date in jwt_token:
                return {'user': user_info}
    
    return None