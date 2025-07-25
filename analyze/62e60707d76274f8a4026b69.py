def point_type(name, fields, srid_map):
    """
    Dynamically create a Point subclass.
    """
    class_attrs = {
        '__slots__': tuple(fields),
        'srid_map': srid_map
    }

    def __init__(self, *args, **kwargs):
        if len(args) > len(fields):
            raise TypeError(f"{name} takes {len(fields)} positional arguments but {len(args)} were given")
            
        # Set positional args
        for field, value in zip(fields, args):
            setattr(self, field, value)
            
        # Set keyword args
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

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return all(getattr(self, f) == getattr(other, f) for f in fields)

    def __hash__(self):
        return hash(tuple(getattr(self, f) for f in fields))

    class_attrs['__init__'] = __init__
    class_attrs['__repr__'] = __repr__
    class_attrs['__eq__'] = __eq__
    class_attrs['__hash__'] = __hash__

    return type(name, (object,), class_attrs)