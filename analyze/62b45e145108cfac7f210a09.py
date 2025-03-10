def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifica che tutti i digest nel manifesto necessari siano presenti e utilizzati.

    :param manifest_files: Lista di file di manifesto che contengono i digest.
    :param digests_used: Set di digest che sono stati utilizzati.
    :return: True se tutti i digest necessari sono presenti e utilizzati, False altrimenti.
    """
    # Estrai tutti i digest dai file di manifesto
    manifest_digests = set()
    for manifest_file in manifest_files:
        with open(manifest_file, 'r') as file:
            for line in file:
                if line.strip():  # Ignora righe vuote
                    manifest_digests.add(line.strip())

    # Verifica che tutti i digest nel manifesto siano stati utilizzati
    return manifest_digests.issubset(digests_used)