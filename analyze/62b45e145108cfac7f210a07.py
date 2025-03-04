def validate(self, inventory, extract_spec_version=False):
    """
    验证给定的库存（inventory）。如果 `extract_spec_version` 为 True，则会根据 `type` 值来确定规范版本。如果没有 `type` 值或其无效，则其他测试将基于 `self.spec_version` 中给定的版本。
    验证给定的库存。

    如果 `extract_spec_version` 为真，则会根据 `type` 值来确定规范版本。
    如果没有 `type` 值或其无效，则其他测试将基于 `self.spec_version` 中给定的版本。
    """
    if not isinstance(inventory, dict):
        raise ValueError("Inventory must be a dictionary")

    # Extract spec version from type if requested
    if extract_spec_version:
        try:
            type_str = inventory.get('type', '')
            if type_str.startswith('inventory:'):
                version = type_str.split(':')[1]
                self.spec_version = version
        except (AttributeError, IndexError):
            pass # Fall back to self.spec_version

    # Validate required fields
    required_fields = ['type', 'items']
    for field in required_fields:
        if field not in inventory:
            raise ValueError(f"Missing required field: {field}")

    # Validate type format
    type_str = inventory['type']
    if not isinstance(type_str, str) or not type_str.startswith('inventory:'):
        raise ValueError("Invalid type format. Must be 'inventory:<version>'")

    # Validate items is a list
    items = inventory['items']
    if not isinstance(items, list):
        raise ValueError("Items must be a list")

    # Validate each item
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("Each item must be a dictionary")
        
        # Validate required item fields based on spec version
        if self.spec_version == '1.0':
            required_item_fields = ['id', 'name', 'quantity']
        else:  # Default to latest version requirements
            required_item_fields = ['id', 'name', 'quantity', 'category']
            
        for field in required_item_fields:
            if field not in item:
                raise ValueError(f"Item missing required field: {field}")

        # Validate field types
        if not isinstance(item['id'], str):
            raise ValueError("Item id must be a string")
        if not isinstance(item['name'], str):
            raise ValueError("Item name must be a string") 
        if not isinstance(item['quantity'], (int, float)):
            raise ValueError("Item quantity must be a number")
        if self.spec_version != '1.0' and not isinstance(item['category'], str):
            raise ValueError("Item category must be a string")

    return True