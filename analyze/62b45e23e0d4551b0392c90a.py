def validate_version_inventories(self, version_dirs):
    """
    Each version SHOULD have an inventory up to that point.

    Also keep a record of any content digests different from those in the root inventory
    so that we can also check them when validating the content.

    version_dirs is an array of version directory names and is assumed to be in
    version sequence (1, 2, 3...).
    """
    inventory_records = {}
    content_digest_discrepancies = {}

    for version_dir in version_dirs:
        inventory_path = os.path.join(version_dir, "inventory.json")
        if not os.path.exists(inventory_path):
            raise FileNotFoundError(f"Inventory file not found for version: {version_dir}")

        with open(inventory_path, 'r') as f:
            inventory = json.load(f)
        
        inventory_records[version_dir] = inventory

        # Compare content digests with root inventory
        root_inventory_path = os.path.join(version_dirs[0], "inventory.json")
        with open(root_inventory_path, 'r') as f:
            root_inventory = json.load(f)
        
        for key, value in inventory.items():
            if key in root_inventory and value != root_inventory[key]:
                content_digest_discrepancies[key] = {
                    'version': version_dir,
                    'root_digest': root_inventory[key],
                    'version_digest': value
                }

    return inventory_records, content_digest_discrepancies