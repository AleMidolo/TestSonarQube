def validate_fixity(self, fixity, manifest_files):
    """
    Convalida l'attributo fixty block nell'inventario.

    Controlla la struttura del blocco di fissità e assicurati che siano referenziati solo i file elencati nel manifesto.
    """
    if not isinstance(fixity, dict):
        raise ValueError("Fixity must be a dictionary.")

    required_keys = {'algorithm', 'checksums'}
    if not required_keys.issubset(fixity.keys()):
        raise ValueError(f"Fixity block must contain the keys: {required_keys}")

    if not isinstance(fixity['checksums'], list):
        raise ValueError("Checksums must be a list.")

    for checksum in fixity['checksums']:
        if not isinstance(checksum, dict):
            raise ValueError("Each checksum must be a dictionary.")
        if 'file' not in checksum or 'value' not in checksum:
            raise ValueError("Each checksum must contain 'file' and 'value' keys.")
        if checksum['file'] not in manifest_files:
            raise ValueError(f"File {checksum['file']} referenced in fixity is not in the manifest.")
    
    return True