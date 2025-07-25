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
            setattr(self, field, value)
            
        # Set default values for unset fields
        for field in fields:
            if not hasattr(self, field):
                setattr(self, field, 0.0)
                
        # Set default SRID
        self.srid = srid_map.get('default', None)
    
    def __repr__(self):
        values = [getattr(self, field) for field in fields]
        fields_str = ', '.join(f"{field}={value}" for field, value in zip(fields, values))
        return f"{name}({fields_str})"
    
    class_attrs['__init__'] = __init__
    class_attrs['__repr__'] = __repr__
    
    return type(name, (), class_attrs)