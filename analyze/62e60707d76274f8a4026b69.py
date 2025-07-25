def point_type(name, fields, srid_map):
    """
    Dynamically create a Point subclass.
    """
    class_attrs = {
        '__slots__': tuple(fields),
        '_srid_map': srid_map
    }

    def __init__(self, *args, **kwargs):
        if len(args) > len(fields):
            raise TypeError(f"{name} takes {len(fields)} positional arguments but {len(args)} were given")
        
        # Set positional arguments
        for field, value in zip(fields, args):
            setattr(self, field, value)
            
        # Set keyword arguments
        for field, value in kwargs.items():
            if field not in fields:
                raise TypeError(f"{name} got an unexpected keyword argument '{field}'")
            if hasattr(self, field):
                raise TypeError(f"Got multiple values for argument '{field}'")
            setattr(self, field, value)
            
        # Check all fields are set
        for field in fields:
            if not hasattr(self, field):
                raise TypeError(f"Missing required argument: '{field}'")

    def __repr__(self):
        args = [f"{field}={getattr(self, field)!r}" for field in fields]
        return f"{name}({', '.join(args)})"

    def transform(self, srid):
        if srid not in self._srid_map:
            raise ValueError(f"Unknown SRID: {srid}")
        return self._srid_map[srid](self)

    class_attrs['__init__'] = __init__
    class_attrs['__repr__'] = __repr__
    class_attrs['transform'] = transform

    return type(name, (), class_attrs)