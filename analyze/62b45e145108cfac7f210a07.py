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
                if type_value.startswith('inventory-'):
                    try:
                        version = type_value.split('-')[1]
                        self.spec_version = version
                    except IndexError:
                        pass

    # Validate required fields based on spec_version
    required_fields = ['id', 'name', 'items']
    
    for field in required_fields:
        if field not in inventory:
            raise ValueError(f"Missing required field: {field}")

    # Validate items is a list
    if not isinstance(inventory['items'], list):
        raise ValueError("'items' must be a list")

    # Validate each item in items list
    for item in inventory['items']:
        if not isinstance(item, dict):
            raise ValueError("Each item must be a dictionary")
        
        # Check required item fields
        item_required_fields = ['id', 'quantity']
        for field in item_required_fields:
            if field not in item:
                raise ValueError(f"Item missing required field: {field}")
            
        # Validate quantity is a positive number
        if not isinstance(item['quantity'], (int, float)) or item['quantity'] < 0:
            raise ValueError("Item quantity must be a positive number")

    return True