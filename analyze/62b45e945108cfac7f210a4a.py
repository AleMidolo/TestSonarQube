def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
    """
    स्टोरेज रूट हाइरार्की को मान्य करें।

    रिटर्न करता है:
        num_objects - जांचे गए ऑब्जेक्ट्स की संख्या
        good_objects - जांचे गए ऑब्जेक्ट्स की संख्या जो मान्य पाए गए
    """
    num_objects = 0
    good_objects = 0
    
    # Walk through all files in hierarchy
    for root, dirs, files in self.walk():
        for filename in files:
            num_objects += 1
            filepath = os.path.join(root, filename)
            
            try:
                # Validate file exists
                if not os.path.exists(filepath):
                    if show_warnings:
                        print(f"Warning: File {filepath} does not exist")
                    continue
                    
                # Validate object if requested
                if validate_objects:
                    with open(filepath, 'rb') as f:
                        data = f.read()
                        
                    # Check file digest if requested
                    if check_digests:
                        stored_digest = self.get_digest(filepath)
                        computed_digest = hashlib.sha256(data).hexdigest()
                        
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