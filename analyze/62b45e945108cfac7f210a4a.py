def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
    """
    स्टोरेज रूट हाइरार्की को मान्य करें।

    रिटर्न करता है:
        num_objects - जांचे गए ऑब्जेक्ट्स की संख्या
        good_objects - जांचे गए ऑब्जेक्ट्स की संख्या जो मान्य पाए गए
    """
    num_objects = 0
    good_objects = 0
    
    # Recursively traverse the hierarchy
    for root, dirs, files in self.walk():
        for file in files:
            num_objects += 1
            
            # Validate each object if requested
            if validate_objects:
                try:
                    obj_path = os.path.join(root, file)
                    
                    # Check file exists
                    if not os.path.exists(obj_path):
                        if show_warnings:
                            print(f"Warning: Object {obj_path} does not exist")
                        continue
                        
                    # Verify digest if requested
                    if check_digests:
                        stored_digest = self.get_digest(obj_path)
                        actual_digest = self.calculate_digest(obj_path)
                        
                        if stored_digest != actual_digest:
                            if show_warnings:
                                print(f"Warning: Digest mismatch for {obj_path}")
                            continue
                    
                    good_objects += 1
                    
                except Exception as e:
                    if show_warnings:
                        print(f"Warning: Error validating {file}: {str(e)}")
                    continue
                    
    return num_objects, good_objects