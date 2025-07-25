def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
    """
    स्टोरेज रूट हाइरार्की को मान्य करें।

    रिटर्न करता है:
        num_objects - जांचे गए ऑब्जेक्ट्स की संख्या
        good_objects - जांचे गए ऑब्जेक्ट्स की संख्या जो मान्य पाए गए
    """
    num_objects = 0
    good_objects = 0
    
    # Recursively walk through all directories
    for root, dirs, files in self.walk():
        for file in files:
            num_objects += 1
            
            # Get full path
            filepath = os.path.join(root, file)
            
            try:
                # Validate object if requested
                if validate_objects:
                    obj = self.get_object(filepath)
                    if obj is None:
                        if show_warnings:
                            print(f"Warning: Could not load object at {filepath}")
                        continue
                        
                # Check digest if requested        
                if check_digests:
                    stored_digest = self.get_digest(filepath)
                    computed_digest = self.compute_digest(filepath)
                    
                    if stored_digest != computed_digest:
                        if show_warnings:
                            print(f"Warning: Digest mismatch for {filepath}")
                        continue
                
                good_objects += 1
                
            except Exception as e:
                if show_warnings:
                    print(f"Warning: Error validating {filepath}: {str(e)}")
                continue
                
    return num_objects, good_objects