def validate(self, inventory, extract_spec_version=False):
    """
    दिए गए इन्वेंटरी को सत्यापित करें।

    यदि `extract_spec_version` का मान `True` है, तो यह `type` मान को देखकर 
    स्पेसिफिकेशन वर्जन निर्धारित करेगा। यदि `type` मान मौजूद नहीं है या यह 
    मान्य नहीं है, तो अन्य परीक्षण `self.spec_version` में दिए गए वर्जन के 
    आधार पर किए जाएंगे।
    """
    if not isinstance(inventory, dict):
        raise ValueError("Inventory must be a dictionary")

    if extract_spec_version:
        if 'type' in inventory:
            type_value = inventory['type']
            if isinstance(type_value, str):
                # Extract version from type value
                if type_value.startswith('STIX '):
                    try:
                        version = type_value.split(' ')[1]
                        self.spec_version = version
                    except IndexError:
                        pass

    # Validate required fields
    required_fields = ['objects']
    for field in required_fields:
        if field not in inventory:
            raise ValueError(f"Missing required field: {field}")

    # Validate objects array
    if not isinstance(inventory['objects'], list):
        raise ValueError("'objects' must be a list")

    # Validate each object in the inventory
    for obj in inventory['objects']:
        if not isinstance(obj, dict):
            raise ValueError("Each object must be a dictionary")
        
        # Check required object fields based on spec version
        required_obj_fields = ['id', 'type']
        for field in required_obj_fields:
            if field not in obj:
                raise ValueError(f"Object missing required field: {field}")

    return True