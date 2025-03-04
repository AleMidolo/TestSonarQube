def point_type(name, fields, srid_map):
    """
    动态创建一个 Point 子类。
    """
    class_attrs = {
        '__slots__': tuple(fields) + ('srid',),
        '_fields': tuple(fields),
        '_srid_map': srid_map
    }

    def __init__(self, *args, **kwargs):
        if len(args) > len(fields):
            raise TypeError(f'Expected {len(fields)} arguments, got {len(args)}')
        
        # Set values from positional args
        for field, value in zip(fields, args):
            setattr(self, field, value)
            
        # Set remaining fields from kwargs
        remaining_fields = set(fields) - {fields[i] for i in range(len(args))}
        for field in remaining_fields:
            if field in kwargs:
                setattr(self, field, kwargs[field])
            else:
                setattr(self, field, None)
                
        # Set SRID
        self.srid = kwargs.get('srid', None)
        
    def __repr__(self):
        field_values = [f'{field}={getattr(self, field)}' for field in fields]
        if self.srid is not None:
            field_values.append(f'srid={self.srid}')
        return f"{name}({', '.join(field_values)})"
    
    class_attrs['__init__'] = __init__
    class_attrs['__repr__'] = __repr__
    
    return type(name, (), class_attrs)