def point_type(name, fields, srid_map):
    """
    डायनामिक रूप से एक पॉइंट सबक्लास बनाएं।

    :param name: सबक्लास का नाम
    :param fields: सबक्लास के फ़ील्ड्स (डिक्शनरी के रूप में)
    :param srid_map: SRID मैपिंग (डिक्शनरी के रूप में)
    :return: बनाई गई सबक्लास
    """
    class PointSubclass:
        def __init__(self, **kwargs):
            for field, value in kwargs.items():
                setattr(self, field, value)
            self.srid = srid_map.get(name, 4326)  # Default SRID is 4326 (WGS84)

        def __repr__(self):
            fields_str = ', '.join(f"{field}={getattr(self, field)}" for field in fields)
            return f"{name}({fields_str}, srid={self.srid})"

    PointSubclass.__name__ = name
    return PointSubclass