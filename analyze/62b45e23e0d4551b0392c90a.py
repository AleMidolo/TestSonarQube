def validate_version_inventories(self, version_dirs):
    """
    Each version SHOULD have an inventory up to that point.

    Also keep a record of any content digests different from those in the root inventory
    so that we can also check them when validating the content.

    version_dirs is an array of version directory names and is assumed to be in
    version sequence (1, 2, 3...).
    """
    # Keep track of digests that differ from root inventory
    different_digests = set()
    
    # Get root inventory for comparison
    root_inventory = self.get_inventory()
    if not root_inventory:
        raise ValueError("No root inventory found")
        
    # Check each version directory
    for version in version_dirs:
        version_inventory = self.get_inventory(version)
        
        if not version_inventory:
            raise ValueError(f"Missing inventory for version {version}")
            
        # Compare digests with root inventory
        for file_path, digest in version_inventory.items():
            if file_path in root_inventory:
                if digest != root_inventory[file_path]:
                    different_digests.add((file_path, digest))
            else:
                # New file not in root inventory
                different_digests.add((file_path, digest))
                
        # Validate that inventory contains all files up to this version
        expected_files = set()
        for v in version_dirs[:version_dirs.index(version) + 1]:
            version_files = self.get_version_files(v)
            expected_files.update(version_files)
            
        inventory_files = set(version_inventory.keys())
        missing_files = expected_files - inventory_files
        
        if missing_files:
            raise ValueError(f"Version {version} inventory missing files: {missing_files}")
            
    return different_digests