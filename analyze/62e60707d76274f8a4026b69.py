def point_type(name, fields, srid_map):
    """
    Dynamically create a Point subclass.

    Args:
        name (str): The name of the new Point subclass.
        fields (dict): A dictionary of field names and their corresponding types.
        srid_map (dict): A dictionary mapping field names to SRID values.

    Returns:
        type: A new Point subclass with the specified fields and SRID mappings.
    """
    class Point:
        def __init__(self, **kwargs):
            for field, value in kwargs.items():
                setattr(self, field, value)
            self.srid_map = srid_map

        def __repr__(self):
            fields_str = ', '.join(f"{field}={getattr(self, field)}" for field in fields)
            return f"{name}({fields_str})"

    Point.__name__ = name
    Point.__qualname__ = name
    Point.__annotations__ = fields

    return Point