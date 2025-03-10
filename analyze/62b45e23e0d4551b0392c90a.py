def validate_version_inventories(self, version_dirs):
    """
    Each version SHOULD have an inventory up to that point.

    Also keep a record of any content digests different from those in the root inventory
    so that we can also check them when validating the content.

    version_dirs is an array of version directory names and is assumed to be in
    version sequence (1, 2, 3...).
    """
    inventory_records = {}
    for version_dir in version_dirs:
        inventory_path = os.path.join(version_dir, "inventory.json")
        if not os.path.exists(inventory_path):
            raise FileNotFoundError(f"Inventory file not found for version: {version_dir}")
        
        with open(inventory_path, 'r') as f:
            inventory = json.load(f)
        
        # Compare with root inventory if exists
        if inventory_records:
            root_inventory = inventory_records.get("root")
            if root_inventory:
                for key, value in inventory.items():
                    if key in root_inventory and value != root_inventory[key]:
                        inventory_records[key] = value
        
        # Record the inventory for this version
        inventory_records[version_dir] = inventory
    
    return inventory_records