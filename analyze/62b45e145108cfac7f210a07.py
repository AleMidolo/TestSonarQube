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
    required_fields = ['id', 'type', 'spec_version', 'objects']
    for field in required_fields:
        if field not in inventory:
            raise ValueError(f"Missing required field: {field}")

    # Validate type
    if inventory['type'] != f"STIX {self.spec_version}":
        raise ValueError(f"Invalid type value. Expected 'STIX {self.spec_version}'")

    # Validate spec_version
    if inventory['spec_version'] != self.spec_version:
        raise ValueError(f"Invalid spec_version. Expected '{self.spec_version}'")

    # Validate objects is a list
    if not isinstance(inventory['objects'], list):
        raise ValueError("'objects' must be a list")

    # Validate ID format
    if not isinstance(inventory['id'], str) or not inventory['id'].startswith('bundle--'):
        raise ValueError("Invalid ID format. Must be string starting with 'bundle--'")

    return True