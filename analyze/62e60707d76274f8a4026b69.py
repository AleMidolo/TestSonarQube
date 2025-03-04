def point_type(name, fields, srid_map):
    """
    动态创建一个 Point 子类。
    """
    class_attrs = {
        '__slots__': tuple(fields) + ('srid',),
        '_srid_map': srid_map
    }

    def __init__(self, *args, **kwargs):
        if len(args) > len(fields):
            raise TypeError(f"Expected {len(fields)} arguments, got {len(args)}")
        
        # Set fields from positional args
        for field, value in zip(fields, args):
            setattr(self, field, value)
            
        # Set fields from keyword args
        for field, value in kwargs.items():
            if field not in fields:
                raise TypeError(f"Unexpected keyword argument '{field}'")
            if hasattr(self, field):
                raise TypeError(f"Multiple values for argument '{field}'")
            setattr(self, field, value)
            
        # Check all fields are set
        for field in fields:
            if not hasattr(self, field):
                raise TypeError(f"Missing required argument: '{field}'")
                
        # Set default SRID
        self.srid = srid_map.get('default', None)
        
    def __repr__(self):
        args = [f"{field}={getattr(self, field)}" for field in fields]
        if self.srid is not None:
            args.append(f"srid={self.srid}")
        return f"{name}({', '.join(args)})"
    
    class_attrs['__init__'] = __init__
    class_attrs['__repr__'] = __repr__
    
    return type(name, (), class_attrs)