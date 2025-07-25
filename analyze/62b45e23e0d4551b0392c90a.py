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

        # Validate that the version inventory is up to date
        if not self.is_inventory_up_to_date(version_inventory, root_inventory):
            raise ValueError(f"Inventory for version {version} is not up to date.")

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

def is_inventory_up_to_date(self, version_inventory, root_inventory):
    # Placeholder for checking if the version inventory is up to date
    return all(item in root_inventory for item in version_inventory)