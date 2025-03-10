def point_type(name, fields, srid_map):
    """
    Dynamically create a Point subclass.

    Args:
        name (str): The name of the new Point subclass.
        fields (dict): A dictionary of field names and their corresponding types.
        srid_map (dict): A dictionary mapping SRID values to coordinate reference systems.

    Returns:
        type: A new Point subclass with the specified fields and SRID mapping.
    """
    class Point:
        def __init__(self, **kwargs):
            for field, field_type in fields.items():
                setattr(self, field, kwargs.get(field))
            self.srid = kwargs.get('srid', None)

        def __repr__(self):
            fields_str = ', '.join(f"{field}={getattr(self, field)}" for field in fields)
            return f"{name}({fields_str}, srid={self.srid})"

        def transform(self, new_srid):
            if self.srid is None:
                raise ValueError("Cannot transform a point with no SRID.")
            if new_srid not in srid_map:
                raise ValueError(f"SRID {new_srid} not found in SRID map.")
            # Placeholder for transformation logic
            self.srid = new_srid
            return self

    Point.__name__ = name
    return Point