def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
    """
    Valida la gerarchia di archiviazione.

    Restituisce:
        num_objects - numero di oggetti verificati
        good_objects - numero di oggetti verificati che sono risultati validi
    """
    num_objects = 0
    good_objects = 0

    # Simulazione della validazione degli oggetti
    for obj in self.storage_hierarchy:
        num_objects += 1
        is_valid = True  # Logica di validazione qui

        if validate_objects:
            # Logica per validare l'oggetto
            pass

        if check_digests:
            # Logica per controllare i digest
            pass

        if is_valid:
            good_objects += 1
        elif show_warnings:
            print(f"Warning: Object {obj} is not valid.")

    return num_objects, good_objects