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
            
            # Validate file exists
            if not os.path.exists(file_path):
                if show_warnings:
                    print(f"Warning: File {file_path} does not exist")
                is_valid = False
                continue
                
            if validate_objects:
                # Validate file can be opened and read
                try:
                    with open(file_path, 'rb') as f:
                        content = f.read()
                except:
                    if show_warnings:
                        print(f"Warning: Could not read file {file_path}")
                    is_valid = False
                    continue
                    
                if check_digests:
                    # Validate checksum if digest file exists
                    digest_path = file_path + '.digest'
                    if os.path.exists(digest_path):
                        try:
                            with open(digest_path, 'r') as f:
                                stored_digest = f.read().strip()
                            calculated_digest = hashlib.sha256(content).hexdigest()
                            if stored_digest != calculated_digest:
                                if show_warnings:
                                    print(f"Warning: Digest mismatch for {file_path}")
                                is_valid = False
                                continue
                        except:
                            if show_warnings:
                                print(f"Warning: Could not validate digest for {file_path}")
                            is_valid = False
                            continue
            
            if is_valid:
                good_objects += 1
                
    return num_objects, good_objects