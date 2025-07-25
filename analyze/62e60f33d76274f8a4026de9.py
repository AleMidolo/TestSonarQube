def dehydrate_point(value):
    """
    Deshidratador para datos de tipo `Point`.

    :param value:
    :type value: Point
    :return:
    """
    if value is None:
        return None
        
    return {
        'x': value.x,
        'y': value.y
    }