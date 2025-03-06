def point_type(name, fields, srid_map):
    """
    डायनामिक रूप से एक पॉइंट सबक्लास बनाएं।

    :param name: सबक्लास का नाम
    :param fields: सबक्लास में शामिल फ़ील्ड्स
    :param srid_map: SRID मैपिंग
    :return: डायनामिक रूप से बनाई गई पॉइंट सबक्लास
    """
    from sqlalchemy import Column, Integer, Float
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    attrs = {
        '__tablename__': name.lower(),
        'id': Column(Integer, primary_key=True)
    }

    for field in fields:
        attrs[field] = Column(Float)

    attrs['srid'] = Column(Integer, default=srid_map.get(name, 4326))

    return type(name, (Base,), attrs)