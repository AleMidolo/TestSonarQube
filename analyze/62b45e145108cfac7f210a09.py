def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifica che tutti i digest nel manifesto necessari siano presenti e utilizzati.
    """
    # Estrai tutti i digest dal manifesto
    manifest_digests = set()
    for manifest_file in manifest_files:
        with open(manifest_file, 'r') as file:
            for line in file:
                if line.strip():  # Ignora righe vuote
                    manifest_digests.add(line.strip())
    
    # Verifica che tutti i digest necessari siano presenti nel manifesto
    missing_digests = set(digests_used) - manifest_digests
    if missing_digests:
        raise ValueError(f"Digests mancanti nel manifesto: {missing_digests}")
    
    # Verifica che tutti i digest nel manifesto siano stati utilizzati
    unused_digests = manifest_digests - set(digests_used)
    if unused_digests:
        raise ValueError(f"Digests non utilizzati nel manifesto: {unused_digests}")
    
    return True