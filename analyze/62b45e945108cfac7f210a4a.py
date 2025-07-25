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
        for file in files:
            num_objects += 1
            file_path = os.path.join(root, file)
            
            is_valid = True
            
            # Validate file exists and is readable
            if not os.path.isfile(file_path):
                if show_warnings:
                    print(f"Warning: {file_path} is not a valid file")
                is_valid = False
                continue
                
            if validate_objects:
                try:
                    with open(file_path, 'rb') as f:
                        # Try reading the file
                        f.read()
                except:
                    if show_warnings:
                        print(f"Warning: {file_path} cannot be read")
                    is_valid = False
                    
            if check_digests and is_valid:
                # Check if digest file exists
                digest_path = file_path + '.digest'
                if not os.path.isfile(digest_path):
                    if show_warnings:
                        print(f"Warning: Missing digest file for {file_path}")
                    is_valid = False
                else:
                    # Validate digest matches file content
                    try:
                        with open(digest_path, 'r') as f:
                            stored_digest = f.read().strip()
                        with open(file_path, 'rb') as f:
                            file_digest = hashlib.sha256(f.read()).hexdigest()
                        if stored_digest != file_digest:
                            if show_warnings:
                                print(f"Warning: Invalid digest for {file_path}")
                            is_valid = False
                    except:
                        if show_warnings:
                            print(f"Warning: Error checking digest for {file_path}")
                        is_valid = False
                        
            if is_valid:
                good_objects += 1
                
    return num_objects, good_objects