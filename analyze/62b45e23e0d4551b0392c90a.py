def validate_version_inventories(self, version_dirs):
    root_inventory = self.load_root_inventory()
    content_digests = {}
    
    for version in version_dirs:
        inventory = self.load_inventory(version)
        
        if not self.validate_inventory(inventory, root_inventory):
            raise ValueError(f"Invalid inventory for version {version}")
        
        for content in inventory:
            if content not in root_inventory or inventory[content] != root_inventory[content]:
                content_digests[content] = inventory[content]
    
    return content_digests

def load_root_inventory(self):
    # Implementation to load the root inventory
    pass

def load_inventory(self, version):
    # Implementation to load the inventory for a specific version
    pass

def validate_inventory(self, inventory, root_inventory):
    # Implementation to validate the inventory against the root inventory
    pass