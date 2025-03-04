def validate(self, path):
    """
    Validate OCFL object at path or pyfs root.
    
    Returns True if valid (warnings permitted), False otherwise.
    """
    try:
        # Check if path exists
        if not os.path.exists(path):
            return False
            
        # Verify OCFL object structure
        if not self._verify_structure(path):
            return False
            
        # Check for required files
        required_files = ['0=ocfl_object_1.0', 'inventory.json', 'inventory.json.sha512'] 
        for file in required_files:
            if not os.path.isfile(os.path.join(path, file)):
                return False
                
        # Validate inventory
        with open(os.path.join(path, 'inventory.json')) as f:
            try:
                inventory = json.load(f)
            except json.JSONDecodeError:
                return False
                
        # Check inventory required fields
        required_fields = ['id', 'type', 'digestAlgorithm', 'versions']
        if not all(field in inventory for field in required_fields):
            return False
            
        # Verify checksums
        if not self._verify_checksums(path, inventory):
            return False
            
        # Verify version sequence
        if not self._verify_versions(inventory['versions']):
            return False
            
        return True
        
    except Exception:
        return False