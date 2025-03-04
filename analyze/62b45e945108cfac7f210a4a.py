def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
    """
    Valida la gerarchia di archiviazione.

    Restituisce:
        num_objects - numero di oggetti verificati
        good_objects - numero di oggetti verificati che sono risultati validi
    """
    num_objects = 0
    good_objects = 0

    # Simulated validation process
    for obj in self.storage_hierarchy:
        num_objects += 1
        is_valid = True  # Replace with actual validation logic

        if validate_objects and not self.validate_object(obj):
            is_valid = False
            if show_warnings:
                print(f"Warning: Object {obj} is invalid.")
        
        if check_digests and not self.check_digest(obj):
            is_valid = False
            if show_warnings:
                print(f"Warning: Digest for object {obj} is invalid.")

        if is_valid:
            good_objects += 1

    return num_objects, good_objects