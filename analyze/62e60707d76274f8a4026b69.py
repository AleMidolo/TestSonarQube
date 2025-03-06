def point_type(name, fields, srid_map):
    """
    डायनामिक रूप से एक पॉइंट सबक्लास बनाएं।

    :param name: सबक्लास का नाम
    :param fields: फील्ड्स की सूची
    :param srid_map: SRID मैपिंग
    :return: डायनामिक रूप से बनाई गई पॉइंट सबक्लास
    """
    from sqlalchemy import Column, Integer, Float
    from sqlalchemy.ext.declarative import declarative_base
    from geoalchemy2 import Geometry

    Base = declarative_base()

    attrs = {
        '__tablename__': name.lower(),
        'id': Column(Integer, primary_key=True)
    }

    for field in fields:
        if field == 'geometry':
            attrs[field] = Column(Geometry(geometry_type='POINT', srid=srid_map.get(field, 4326)))
        else:
            attrs[field] = Column(Float)

    PointSubclass = type(name, (Base,), attrs)
    return PointSubclass