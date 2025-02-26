def dehydrate_point(value):  
    """
    Deshidratador para datos de tipo `Point`.  

    :param value: Un objeto de tipo Point que se desea deshidratar.
    :type value: Point  
    :return: Un diccionario con las coordenadas del punto.
    """
    if not isinstance(value, Point):
        raise ValueError("El valor debe ser una instancia de Point.")
    
    return {
        'x': value.x,
        'y': value.y
    }