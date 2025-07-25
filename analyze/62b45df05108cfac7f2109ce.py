def validate(self, path):
    """
    Validate OCFL object at path or pyfs root.
    
    Returns True if valid (warnings permitted), False otherwise.
    """
    try:
        # Check if path exists
        if not os.path.exists(path):
            return False
            
        # Verify OCFL structure
        if not self._verify_ocfl_structure(path):
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
        for field in required_fields:
            if field not in inventory:
                return False
                
        # Verify checksums
        if not self._verify_checksums(path, inventory):
            return False
            
        # Verify version sequence
        versions = sorted(inventory['versions'].keys())
        for i, v in enumerate(versions, 1):
            if f'v{i}' != v:
                return False
                
        # All validation passed
        return True
        
    except Exception:
        return False