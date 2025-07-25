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
        raise ValueError("Root inventory not found")
        
    # Check each version directory
    for version in version_dirs:
        version_inventory_path = os.path.join(version, "inventory.txt")
        
        # Verify inventory exists for this version
        if not os.path.exists(version_inventory_path):
            raise ValueError(f"Missing inventory for version {version}")
            
        # Load version inventory
        version_inventory = self.load_inventory(version_inventory_path)
        
        # Compare digests with root inventory
        for file_path, digest in version_inventory.items():
            if file_path in root_inventory:
                if digest != root_inventory[file_path]:
                    different_digests.add((file_path, digest))
            else:
                different_digests.add((file_path, digest))
                
    # Store different digests for later content validation
    self.different_digests = different_digests
    
    return True