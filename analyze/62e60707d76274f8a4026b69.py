def point_type(name, fields, srid_map):
    """
    डायनामिक रूप से एक पॉइंट सबक्लास बनाएं।

    :param name: सबक्लास का नाम
    :param fields: सबक्लास में शामिल करने के लिए फ़ील्ड्स
    :param srid_map: SRID मैपिंग
    :return: डायनामिक रूप से बनाई गई पॉइंट सबक्लास
    """
    from collections import namedtuple

    # SRID मैपिंग को फ़ील्ड्स में जोड़ें
    fields_with_srid = fields + ('srid',)

    # नामित टपल (namedtuple) बनाएं
    PointSubclass = namedtuple(name, fields_with_srid)

    # SRID मैपिंग को सबक्लास में जोड़ें
    PointSubclass.srid_map = srid_map

    return PointSubclass