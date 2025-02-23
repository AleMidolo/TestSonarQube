def validate_fixity(self, fixity, manifest_files):
    """
    Convalida l'attributo fixty block nell'inventario.

    Controlla la struttura del blocco di fissità e assicurati che siano referenziati solo i file elencati nel manifesto.
    """
    if not isinstance(fixity, dict):
        raise ValueError("Fixity must be a dictionary.")

    if 'files' not in fixity:
        raise ValueError("Fixity block must contain 'files' key.")

    fixity_files = fixity['files']
    
    if not isinstance(fixity_files, list):
        raise ValueError("Fixity 'files' must be a list.")

    for file in fixity_files:
        if file not in manifest_files:
            raise ValueError(f"File '{file}' in fixity is not referenced in the manifest.")
    
    return True