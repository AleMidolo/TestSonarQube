def dehydrate_point(value):
    """
    结构类是根据值的长度生成的。
    用于处理 Point 数据的转换器

    :param value: 
    :type value: Point 
    :return:
    """
    if value is None:
        return None
        
    # Convert Point object to list of coordinates
    try:
        coords = [value.x, value.y]
        # Add z coordinate if it exists
        if hasattr(value, 'z'):
            coords.append(value.z)
        return coords
    except AttributeError:
        # If value is already a list/tuple of coordinates, return as is
        if isinstance(value, (list, tuple)):
            return list(value)
        raise ValueError("Input must be a Point object or sequence of coordinates")