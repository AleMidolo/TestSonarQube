def xml_children_as_dict(node):
    """
    नोड <xml> के बच्चों को एक डिक्शनरी में बदलें, जो टैग नाम द्वारा कुंजीबद्ध हो।

    यह केवल एक सतही रूपांतरण है - चाइल्ड नोड्स को पुनरावर्ती (recursively) प्रोसेस नहीं किया जाता है।
    """
    return {child.tag: child for child in node}