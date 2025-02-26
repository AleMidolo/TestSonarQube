def point_type(name, fields, srid_map):
    """
    动态创建一个 Point 子类。
    """
    from types import new_class

    def init(self, **kwargs):
        for field in fields:
            setattr(self, field, kwargs.get(field))

    attrs = {'__init__': init}
    point_class = new_class(name, (object,), attrs)

    for srid, field in srid_map.items():
        setattr(point_class, f'srid_{srid}', field)

    return point_class