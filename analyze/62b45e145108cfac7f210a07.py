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
                if type_value.startswith('v'):
                    try:
                        version = float(type_value[1:])
                        self.spec_version = version
                    except ValueError:
                        pass # Use default spec_version if conversion fails

    # Validate required fields based on spec_version
    required_fields = ['id', 'name']
    if self.spec_version >= 2.0:
        required_fields.extend(['description', 'category'])

    for field in required_fields:
        if field not in inventory:
            raise ValueError(f"Missing required field: {field}")
        if not inventory[field]:  # Check for empty values
            raise ValueError(f"Field '{field}' cannot be empty")

    # Validate data types
    if not isinstance(inventory['id'], (str, int)):
        raise ValueError("'id' must be string or integer")
    if not isinstance(inventory['name'], str):
        raise ValueError("'name' must be string")

    if self.spec_version >= 2.0:
        if not isinstance(inventory['description'], str):
            raise ValueError("'description' must be string")
        if not isinstance(inventory['category'], str):
            raise ValueError("'category' must be string")

    # Additional validation can be added based on specific requirements

    return True