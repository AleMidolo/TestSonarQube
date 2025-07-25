def point_type(name, fields, srid_map):
    """
    动态创建一个 Point 子类。
    """
    class_attrs = {
        '__slots__': tuple(fields) + ('srid',),
        '__init__': lambda self, *args: self._init(*args),
        '_init': lambda self, *args: [setattr(self, f, v) for f, v in zip(fields + ('srid',), args)],
        '__repr__': lambda self: f"{name}({', '.join(str(getattr(self, f)) for f in fields + ('srid',))})",
        'srid_map': srid_map
    }
    
    return type(name, (), class_attrs)