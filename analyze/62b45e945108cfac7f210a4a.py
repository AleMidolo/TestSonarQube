def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
    """
    Validate storage root hierarchy.

    Returns:
        num_objects - number of objects checked
        good_objects - number of objects checked that were found to be valid
    """
    num_objects = 0
    good_objects = 0

    # Walk through all directories recursively
    for root, dirs, files in os.walk(self.root_path):
        for filename in files:
            filepath = os.path.join(root, filename)
            num_objects += 1

            try:
                # Validate individual object if requested
                if validate_objects:
                    is_valid = True
                    
                    # Check file exists and is readable
                    if not os.path.isfile(filepath):
                        is_valid = False
                        if show_warnings:
                            print(f"Warning: File {filepath} does not exist or is not accessible")
                    
                    # Validate checksum if requested
                    if check_digests and is_valid:
                        stored_digest = self._get_stored_digest(filepath)
                        calculated_digest = self._calculate_digest(filepath)
                        
                        if stored_digest != calculated_digest:
                            is_valid = False
                            if show_warnings:
                                print(f"Warning: Digest mismatch for {filepath}")
                    
                    if is_valid:
                        good_objects += 1
                        
                else:
                    # If not validating objects, just count them as good
                    good_objects += 1
                    
            except Exception as e:
                if show_warnings:
                    print(f"Warning: Error validating {filepath}: {str(e)}")
                continue

    return num_objects, good_objects