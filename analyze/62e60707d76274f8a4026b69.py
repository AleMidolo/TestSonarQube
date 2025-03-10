def point_type(name, fields, srid_map):
    """
    डायनामिक रूप से एक पॉइंट सबक्लास बनाएं।

    :param name: सबक्लास का नाम
    :param fields: सबक्लास के फ़ील्ड्स (डिक्शनरी के रूप में)
    :param srid_map: SRID मैपिंग (डिक्शनरी के रूप में)
    :return: बनाया गया पॉइंट सबक्लास
    """
    from sqlalchemy import Column, Integer, Float
    from sqlalchemy.ext.declarative import declarative_base
    from geoalchemy2 import Geometry

    Base = declarative_base()

    attrs = {
        '__tablename__': name.lower(),
        'id': Column(Integer, primary_key=True),
        'geom': Column(Geometry(geometry_type='POINT', srid=srid_map.get('default', 4326)))
    }

    for field_name, field_type in fields.items():
        if field_type == 'int':
            attrs[field_name] = Column(Integer)
        elif field_type == 'float':
            attrs[field_name] = Column(Float)
        else:
            raise ValueError(f"असमर्थित फ़ील्ड प्रकार: {field_type}")

    PointSubclass = type(name, (Base,), attrs)
    return PointSubclass