def validate_version_inventories(self, version_dirs):
    """
    Each version SHOULD have an inventory up to that point.

    Also keep a record of any content digests different from those in the root inventory
    so that we can also check them when validating the content.

    version_dirs is an array of version directory names and is assumed to be in
    version sequence (1, 2, 3...).
    """
    root_inventory = self.load_inventory('root_inventory.json')
    content_digests = {}

    for version in version_dirs:
        inventory_path = f"{version}/inventory.json"
        version_inventory = self.load_inventory(inventory_path)

        # Validate that the version inventory matches the expected structure
        if not self.validate_inventory_structure(version_inventory):
            raise ValueError(f"Invalid inventory structure in {inventory_path}")

        # Check for content digests that differ from the root inventory
        for item, digest in version_inventory.items():
            if item in root_inventory and root_inventory[item] != digest:
                content_digests[item] = digest

    return content_digests

def load_inventory(self, path):
    # Placeholder for loading inventory from a JSON file
    import json
    with open(path, 'r') as file:
        return json.load(file)

def validate_inventory_structure(self, inventory):
    # Placeholder for validating the structure of the inventory
    return isinstance(inventory, dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in inventory.items())