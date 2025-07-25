def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
    """
    Valida la gerarchia di archiviazione.

    Restituisce:
        num_objects - numero di oggetti verificati
        good_objects - numero di oggetti verificati che sono risultati validi
    """
    num_objects = 0
    good_objects = 0

    # Attraversa ricorsivamente la gerarchia
    for root, dirs, files in self.walk():
        for file in files:
            num_objects += 1
            
            # Verifica l'oggetto se richiesto
            if validate_objects:
                try:
                    # Verifica il digest se richiesto
                    if check_digests:
                        if self.verify_digest(file):
                            good_objects += 1
                    else:
                        # Se non verifichiamo i digest, consideriamo valido l'oggetto
                        good_objects += 1
                except Exception as e:
                    if show_warnings:
                        print(f"Warning: Failed to validate {file}: {str(e)}")
            else:
                # Se non verifichiamo gli oggetti, li consideriamo tutti validi
                good_objects += 1

    return num_objects, good_objects