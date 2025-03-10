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
        if version_dir == version_dirs[0]:
            root_inventory = inventory
        else:
            for key, value in inventory.items():
                if key in root_inventory and root_inventory[key] != value:
                    inventory_records[key] = value
        
        # Validate that the inventory contains all previous versions' content
        for prev_version in version_dirs[:version_dirs.index(version_dir)]:
            prev_inventory_path = os.path.join(prev_version, "inventory.json")
            with open(prev_inventory_path, 'r') as f:
                prev_inventory = json.load(f)
            for key, value in prev_inventory.items():
                if key not in inventory:
                    raise ValueError(f"Content {key} from version {prev_version} missing in version {version_dir}")
    
    return inventory_records