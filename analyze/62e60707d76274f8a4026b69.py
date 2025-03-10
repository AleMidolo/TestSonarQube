def point_type(name, fields, srid_map):
    """
    डायनामिक रूप से एक पॉइंट सबक्लास बनाएं।

    :param name: सबक्लास का नाम
    :param fields: सबक्लास में शामिल करने के लिए फ़ील्ड्स
    :param srid_map: SRID मैपिंग
    :return: निर्मित सबक्लास
    """
    class PointSubclass:
        def __init__(self, **kwargs):
            for field in fields:
                setattr(self, field, kwargs.get(field))
            self.srid = srid_map.get(name, 4326)  # Default SRID is 4326 (WGS84)

        def __repr__(self):
            fields_str = ', '.join(f"{field}={getattr(self, field)}" for field in fields)
            return f"{name}({fields_str}, srid={self.srid})"

    PointSubclass.__name__ = name
    return PointSubclass