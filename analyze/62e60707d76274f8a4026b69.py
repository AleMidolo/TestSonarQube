def point_type(name, fields, srid_map):
    """
    डायनामिक रूप से एक पॉइंट सबक्लास बनाएं।

    :param name: सबक्लास का नाम
    :param fields: सबक्लास में शामिल करने के लिए फ़ील्ड्स
    :param srid_map: SRID मैपिंग
    :return: डायनामिक रूप से बनाई गई पॉइंट सबक्लास
    """
    from sqlalchemy import Column, Integer, Float
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class Point(Base):
        __tablename__ = name.lower()
        id = Column(Integer, primary_key=True)
        x = Column(Float)
        y = Column(Float)

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f"<Point(x={self.x}, y={self.y})>"

    for field_name, field_type in fields.items():
        setattr(Point, field_name, Column(field_type))

    Point.srid_map = srid_map

    return Point