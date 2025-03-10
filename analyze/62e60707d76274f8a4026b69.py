def point_type(name, fields, srid_map):
    """
    डायनामिक रूप से एक पॉइंट सबक्लास बनाएं।

    :param name: सबक्लास का नाम
    :param fields: सबक्लास में शामिल करने के लिए फ़ील्ड्स
    :param srid_map: SRID मैपिंग
    :return: डायनामिक रूप से बनाई गई पॉइंट सबक्लास
    """
    from django.contrib.gis.db import models

    class Meta:
        app_label = 'your_app_label'  # Replace with your app label

    attrs = {
        '__module__': __name__,
        'Meta': Meta,
    }

    for field_name, field_type in fields.items():
        attrs[field_name] = field_type

    attrs['srid_map'] = srid_map

    return type(name, (models.PointField,), attrs)