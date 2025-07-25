def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifica che tutti i digest nel manifesto necessari siano presenti e utilizzati.
    
    :param manifest_files: Lista di file di manifesto che contengono i digest.
    :param digests_used: Lista di digest che devono essere presenti e utilizzati.
    :return: True se tutti i digest sono presenti e utilizzati, False altrimenti.
    """
    # Estrai tutti i digest dai file di manifesto
    manifest_digests = set()
    for file in manifest_files:
        with open(file, 'r') as f:
            for line in f:
                if line.strip():  # Ignora righe vuote
                    manifest_digests.add(line.strip())
    
    # Verifica che tutti i digest richiesti siano presenti nel manifesto
    for digest in digests_used:
        if digest not in manifest_digests:
            return False
    
    return True