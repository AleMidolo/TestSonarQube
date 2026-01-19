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
        # Verificar si tiene JWT válido
        jwt_token = authorization.get('jwt')
        if jwt_token:
            # Validar que el JWT contenga la fecha de hoy
            today_str = str(datetime.date.today())
            if today_str in jwt_token:
                # Retornar la información del usuario
                user_info = authorization.get('user')
                if user_info:
                    return {'user': user_info}
    
    return None