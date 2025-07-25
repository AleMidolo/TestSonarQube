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
            pass # Fall back to self.spec_version

    # Validate required fields
    required_fields = ['id', 'type', 'items']
    for field in required_fields:
        if field not in inventory:
            raise ValueError(f"Missing required field: {field}")

    # Validate type field format
    if not inventory['type'].startswith('inventory/'):
        raise ValueError("Type field must start with 'inventory/'")

    # Validate items is a list
    if not isinstance(inventory['items'], list):
        raise ValueError("Items field must be a list")

    # Validate each item in items list
    for item in inventory['items']:
        if not isinstance(item, dict):
            raise ValueError("Each item must be a dictionary")
        
        # Validate required item fields
        required_item_fields = ['id', 'type']
        for field in required_item_fields:
            if field not in item:
                raise ValueError(f"Missing required field in item: {field}")

    return True