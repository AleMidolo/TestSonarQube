def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifica che tutti i digest nel manifesto necessari siano presenti e utilizzati.
    
    Args:
        manifest_files (list): Lista dei file del manifesto.
        digests_used (set): Set dei digest utilizzati.
    
    Returns:
        bool: True se tutti i digest necessari sono presenti e utilizzati, False altrimenti.
    """
    # Estrai tutti i digest dal manifesto
    manifest_digests = set()
    for file in manifest_files:
        if 'digest' in file:
            manifest_digests.add(file['digest'])
    
    # Verifica che tutti i digest nel manifesto siano presenti in digests_used
    return manifest_digests.issubset(digests_used)