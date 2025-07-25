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

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return all(getattr(self, field) == getattr(other, field) for field in fields)

    def transform(self, target_srid):
        """Transform point coordinates to a different SRID."""
        if target_srid not in srid_map:
            raise ValueError(f"Unsupported SRID: {target_srid}")
        transform_func = srid_map[target_srid]
        transformed = transform_func(self)
        return type(self)(**{field: getattr(transformed, field) for field in fields})

    class_attrs['__init__'] = __init__
    class_attrs['__repr__'] = __repr__
    class_attrs['__eq__'] = __eq__
    class_attrs['transform'] = transform

    # Create and return the new class
    return type(name, (), class_attrs)