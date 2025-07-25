def point_type(name, fields, srid_map):
    """
    动态创建一个 Point 子类。

    :param name: 类的名称
    :param fields: 类的字段，通常是一个字典，键为字段名，值为字段类型
    :param srid_map: 一个字典，键为字段名，值为 SRID（空间参考系统标识符）
    :return: 动态创建的 Point 子类
    """
    class Point:
        def __init__(self, **kwargs):
            for field, value in kwargs.items():
                setattr(self, field, value)
            self.srid_map = srid_map

        def __repr__(self):
            fields_str = ', '.join(f"{field}={getattr(self, field)}" for field in self.__dict__ if field != 'srid_map')
            return f"{name}({fields_str})"

    Point.__name__ = name
    Point.__qualname__ = name
    Point.__annotations__ = fields

    return Point