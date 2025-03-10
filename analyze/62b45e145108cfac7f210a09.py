def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifica che tutti i digest nel manifesto necessari siano presenti e utilizzati.

    Args:
        manifest_files (list): Lista dei file del manifesto.
        digests_used (set): Insieme dei digest utilizzati.

    Returns:
        bool: True se tutti i digest necessari sono presenti e utilizzati, False altrimenti.
    """
    # Estrai tutti i digest presenti nei file del manifesto
    manifest_digests = set()
    for file in manifest_files:
        with open(file, 'r') as f:
            for line in f:
                if line.strip():  # Ignora righe vuote
                    manifest_digests.add(line.strip())

    # Verifica che tutti i digest necessari siano presenti nel manifesto
    if not digests_used.issubset(manifest_digests):
        return False

    # Verifica che tutti i digest nel manifesto siano stati utilizzati
    if not manifest_digests.issubset(digests_used):
        return False

    return True