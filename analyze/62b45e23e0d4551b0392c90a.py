def validate_version_inventories(self, version_dirs):
    """
    Each version SHOULD have an inventory up to that point.

    Also keep a record of any content digests different from those in the root inventory
    so that we can also check them when validating the content.

    version_dirs is an array of version directory names and is assumed to be in
    version sequence (1, 2, 3...).
    """
    root_inventory = self.get_root_inventory()  # Assume this method exists to get the root inventory
    content_digest_differences = {}

    for version_dir in version_dirs:
        version_inventory = self.get_version_inventory(version_dir)  # Assume this method exists to get the version inventory
        
        # Check if the version inventory exists
        if not version_inventory:
            raise ValueError(f"Inventory missing for version: {version_dir}")
        
        # Compare content digests with root inventory
        for content_id, digest in version_inventory.items():
            if content_id in root_inventory:
                if digest != root_inventory[content_id]:
                    content_digest_differences[content_id] = {
                        'root_digest': root_inventory[content_id],
                        'version_digest': digest,
                        'version': version_dir
                    }
            else:
                content_digest_differences[content_id] = {
                    'root_digest': None,
                    'version_digest': digest,
                    'version': version_dir
                }
    
    return content_digest_differences