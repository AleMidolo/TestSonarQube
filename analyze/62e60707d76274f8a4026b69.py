def point_type(name, fields, srid_map):
    """
    动态创建一个 Point 子类。

    :param name: 类的名称
    :param fields: 类的字段，以字典形式提供，键为字段名，值为字段类型
    :param srid_map: SRID 映射，以字典形式提供，键为字段名，值为 SRID
    :return: 动态创建的 Point 子类
    """
    class Point:
        def __init__(self, **kwargs):
            for field, value in kwargs.items():
                setattr(self, field, value)

        def __repr__(self):
            fields_str = ', '.join(f"{field}={getattr(self, field)}" for field in fields)
            return f"{name}({fields_str})"

        def to_wkt(self):
            coords = []
            for field in fields:
                if field in srid_map:
                    coords.append(f"{getattr(self, field)} {srid_map[field]}")
                else:
                    coords.append(str(getattr(self, field)))
            return f"POINT({', '.join(coords)})"

    Point.__name__ = name
    return Point