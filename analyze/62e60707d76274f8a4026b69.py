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
    from shapely.geometry import Point

    class DynamicPoint(Point):
        __slots__ = tuple(fields.keys())

        def __init__(self, *args, **kwargs):
            super().__init__()
            for field, value in zip(fields.keys(), args):
                setattr(self, field, value)
            for field, value in kwargs.items():
                setattr(self, field, value)

        @property
        def srid(self):
            return srid_map.get(self.__class__.__name__, None)

    DynamicPoint.__name__ = name
    return DynamicPoint