def point_type(name, fields, srid_map):
    """
    动态创建一个 Point 子类。

    Args:
        name (str): 新类的名称。
        fields (dict): 类的字段及其类型。
        srid_map (dict): SRID 映射，用于指定不同坐标系的 SRID 值。

    Returns:
        type: 动态创建的 Point 子类。
    """
    class Point:
        def __init__(self, **kwargs):
            for field, field_type in fields.items():
                setattr(self, field, kwargs.get(field, None))
            self.srid = srid_map.get(kwargs.get('srid', None), None)

        def __repr__(self):
            fields_str = ', '.join(f"{field}={getattr(self, field)}" for field in fields)
            return f"{name}({fields_str}, srid={self.srid})"

    Point.__name__ = name
    return Point