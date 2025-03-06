def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifica che tutti i digest nel manifesto necessari siano presenti e utilizzati.

    :param manifest_files: Lista di file del manifesto che contengono i digest.
    :param digests_used: Set di digest che sono stati utilizzati.
    :return: True se tutti i digest necessari sono presenti e utilizzati, False altrimenti.
    """
    # Estrai tutti i digest necessari dai file del manifesto
    required_digests = set()
    for manifest_file in manifest_files:
        with open(manifest_file, 'r') as file:
            for line in file:
                if line.strip():  # Ignora righe vuote
                    required_digests.add(line.strip())

    # Verifica che tutti i digest necessari siano presenti e utilizzati
    missing_digests = required_digests - digests_used
    unused_digests = digests_used - required_digests

    if missing_digests:
        print(f"Digest mancanti: {missing_digests}")
        return False
    if unused_digests:
        print(f"Digest non utilizzati: {unused_digests}")
        return False

    return True