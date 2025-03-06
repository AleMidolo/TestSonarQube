def xml_children_as_dict(node):
    """
    नोड <xml> के बच्चों को एक डिक्शनरी में बदलें, जो टैग नाम द्वारा कुंजीबद्ध हो।

    यह केवल एक सतही रूपांतरण है - चाइल्ड नोड्स को पुनरावर्ती (recursively) प्रोसेस नहीं किया जाता है।
    """
    result = {}
    for child in node:
        tag = child.tag
        if tag in result:
            if isinstance(result[tag], list):
                result[tag].append(child.text)
            else:
                result[tag] = [result[tag], child.text]
        else:
            result[tag] = child.text
    return result