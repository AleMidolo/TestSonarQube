def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifica che tutti i digest nel manifesto necessari siano presenti e utilizzati.

    :param manifest_files: Lista di file del manifesto contenenti i digest.
    :param digests_used: Set di digest che sono stati utilizzati.
    :return: True se tutti i digest necessari sono presenti e utilizzati, False altrimenti.
    """
    # Estrai tutti i digest presenti nei file del manifesto
    manifest_digests = set()
    for file in manifest_files:
        with open(file, 'r') as f:
            for line in f:
                digest = line.strip()
                if digest:
                    manifest_digests.add(digest)
    
    # Verifica che tutti i digest nel manifesto siano stati utilizzati
    return manifest_digests.issubset(digests_used)