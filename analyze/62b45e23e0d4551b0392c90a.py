def validate_version_inventories(self, version_dirs):
    """
    Each version SHOULD have an inventory up to that point.

    Also keep a record of any content digests different from those in the root inventory
    so that we can also check them when validating the content.

    version_dirs is an array of version directory names and is assumed to be in
    version sequence (1, 2, 3...).
    """
    root_inventory = self.load_root_inventory()
    content_digests = {}

    for version in version_dirs:
        inventory = self.load_inventory(version)
        
        if not self.validate_inventory(inventory, root_inventory):
            raise ValueError(f"Invalid inventory for version {version}")

        # Check for content digests that differ from the root inventory
        for item, digest in inventory.items():
            if item in root_inventory and root_inventory[item] != digest:
                content_digests[item] = digest

    return content_digests

def load_root_inventory(self):
    # Placeholder for loading the root inventory
    pass

def load_inventory(self, version):
    # Placeholder for loading the inventory for a specific version
    pass

def validate_inventory(self, inventory, root_inventory):
    # Placeholder for validating the inventory against the root inventory
    pass