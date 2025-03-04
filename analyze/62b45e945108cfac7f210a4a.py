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

        if validate_objects:
            # Perform object validation
            is_valid = self.validate_object(obj)

        if check_digests:
            # Perform digest check
            is_valid = is_valid and self.check_digest(obj)

        if is_valid:
            good_objects += 1
        elif show_warnings:
            print(f"Warning: Object {obj} is invalid.")

    return num_objects, good_objects