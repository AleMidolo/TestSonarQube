def point_type(name, fields, srid_map):
    """
    Dynamically create a Point subclass.

    Args:
        name (str): The name of the new Point subclass.
        fields (dict): A dictionary of field names and their types.
        srid_map (dict): A dictionary mapping SRID values to coordinate reference systems.

    Returns:
        type: A new Point subclass with the specified fields and SRID mapping.
    """
    class Point:
        def __init__(self, **kwargs):
            for field, value in kwargs.items():
                setattr(self, field, value)
            self.srid = srid_map.get(kwargs.get('srid', None))

        def __repr__(self):
            fields_str = ', '.join(f"{field}={getattr(self, field)}" for field in fields)
            return f"{name}({fields_str}, srid={self.srid})"

    Point.__name__ = name
    return Point