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

    if not isinstance(fixity['checksums'], dict):
        raise ValueError("Checksums must be a dictionary.")

    for file, checksum in fixity['checksums'].items():
        if file not in manifest_files:
            raise ValueError(f"File '{file}' referenced in fixity is not in the manifest.")
        if not isinstance(checksum, str):
            raise ValueError(f"Checksum for file '{file}' must be a string.")

    return True