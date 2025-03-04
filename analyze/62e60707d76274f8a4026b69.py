def point_type(name, fields, srid_map):
    """
    动态创建一个 Point 子类。
    """
    class_attrs = {
        '__slots__': tuple(fields) + ('srid',),
        '__init__': lambda self, *args: (
            setattr(self, 'srid', srid_map.get(len(args), 0)) or
            [setattr(self, f, v) for f, v in zip(fields, args)]
        ),
        '__repr__': lambda self: f"{name}({', '.join(str(getattr(self, f)) for f in fields)})",
        '__eq__': lambda self, other: (
            isinstance(other, type(self)) and
            all(getattr(self, f) == getattr(other, f) for f in fields)
        ),
        '__hash__': lambda self: hash(tuple(getattr(self, f) for f in fields))
    }
    
    return type(name, (), class_attrs)