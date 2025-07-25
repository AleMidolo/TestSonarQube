import os
import re

class OCFLValidator:
    def validate(self, path):
        """
        पथ या pyfs रूट पर OCFL ऑब्जेक्ट को मान्य करें।

        यदि मान्य है (चेतावनियाँ स्वीकार्य हैं), तो True लौटाता है, अन्यथा False।
        """
        if not os.path.exists(path):
            return False
        
        # Check for the presence of required OCFL files and directories
        required_files = ['inventory.json', 'inventory.json.sha512']
        required_dirs = ['v1']
        
        for file in required_files:
            if not os.path.isfile(os.path.join(path, file)):
                return False
        
        for dir in required_dirs:
            if not os.path.isdir(os.path.join(path, dir)):
                return False
        
        # Validate the inventory.json file
        inventory_path = os.path.join(path, 'inventory.json')
        if not self._validate_inventory(inventory_path):
            return False
        
        return True
    
    def _validate_inventory(self, inventory_path):
        """
        Validate the inventory.json file.
        """
        try:
            with open(inventory_path, 'r') as f:
                inventory = json.load(f)
                
            # Check for required fields in inventory.json
            required_fields = ['id', 'type', 'digestAlgorithm', 'head', 'manifest', 'versions']
            for field in required_fields:
                if field not in inventory:
                    return False
                
            # Validate the digestAlgorithm
            if inventory['digestAlgorithm'] != 'sha512':
                return False
                
            # Validate the manifest
            if not isinstance(inventory['manifest'], dict):
                return False
                
            # Validate the versions
            if not isinstance(inventory['versions'], dict):
                return False
                
            return True
        except Exception as e:
            return False