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
                # Validate individual object
                if validate_objects:
                    # Check file exists
                    if not os.path.exists(filepath):
                        if show_warnings:
                            print(f"Warning: File {filepath} does not exist")
                        continue

                    # Check file is readable
                    if not os.access(filepath, os.R_OK):
                        if show_warnings:
                            print(f"Warning: File {filepath} is not readable")
                        continue

                    # Check file size > 0
                    if os.path.getsize(filepath) == 0:
                        if show_warnings:
                            print(f"Warning: File {filepath} is empty")
                        continue

                    # Validate checksum if requested
                    if check_digests:
                        stored_digest = self._get_stored_digest(filepath)
                        if stored_digest:
                            computed_digest = self._compute_digest(filepath)
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