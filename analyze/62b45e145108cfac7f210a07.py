def validate(self, inventory, extract_spec_version=False):
    """
    Validate a given inventory.

    If extract_spec_version is True then will look at the type value to determine
    the specification version. In the case that there is no type value or it isn't
    valid, then other tests will be based on the version given in self.spec_version.
    """
    if not isinstance(inventory, dict):
        raise ValueError("Inventory must be a dictionary")

    # Extract spec version from type if requested
    if extract_spec_version:
        try:
            inv_type = inventory.get('type', '')
            if inv_type.startswith('inventory/'):
                self.spec_version = inv_type.split('/')[1]
        except (AttributeError, IndexError):
            pass

    # Validate required fields
    required_fields = ['name', 'items']
    for field in required_fields:
        if field not in inventory:
            raise ValueError(f"Missing required field: {field}")

    # Validate name is string
    if not isinstance(inventory['name'], str):
        raise ValueError("Inventory name must be a string")

    # Validate items is list
    if not isinstance(inventory['items'], list):
        raise ValueError("Items must be a list")

    # Validate each item
    for item in inventory['items']:
        if not isinstance(item, dict):
            raise ValueError("Each item must be a dictionary")
        
        # Check required item fields
        required_item_fields = ['id', 'quantity']
        for field in required_item_fields:
            if field not in item:
                raise ValueError(f"Item missing required field: {field}")

        # Validate item field types
        if not isinstance(item['id'], str):
            raise ValueError("Item id must be a string")
        if not isinstance(item['quantity'], (int, float)):
            raise ValueError("Item quantity must be a number")
        if item['quantity'] < 0:
            raise ValueError("Item quantity cannot be negative")

    return True