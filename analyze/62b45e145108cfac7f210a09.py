def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifica che tutti i digest nel manifesto necessari siano presenti e utilizzati.
    
    Args:
        manifest_files (list): Lista di file di manifesto.
        digests_used (set): Set di digest utilizzati.
    
    Returns:
        bool: True se tutti i digest necessari sono presenti e utilizzati, False altrimenti.
    """
    # Estrai tutti i digest necessari dai file di manifesto
    required_digests = set()
    for manifest_file in manifest_files:
        with open(manifest_file, 'r') as file:
            for line in file:
                if line.strip():  # Ignora righe vuote
                    required_digests.add(line.strip())
    
    # Verifica che tutti i digest necessari siano presenti e utilizzati
    return required_digests.issubset(digests_used)