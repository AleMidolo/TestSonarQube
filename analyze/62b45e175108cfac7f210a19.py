def validate_fixity(self, fixity, manifest_files):
    """
    Convalida l'attributo fixty block nell'inventario.

    Controlla la struttura del blocco di fissità e assicurati che siano referenziati solo i file elencati nel manifesto.
    """
    if not isinstance(fixity, dict):
        raise ValueError("Fixity must be a dictionary.")
    
    required_keys = {'algorithm', 'hashes'}
    if not required_keys.issubset(fixity.keys()):
        raise ValueError(f"Fixity must contain the keys: {required_keys}")

    if not isinstance(fixity['hashes'], dict):
        raise ValueError("Hashes must be a dictionary.")

    for file, hash_value in fixity['hashes'].items():
        if file not in manifest_files:
            raise ValueError(f"File '{file}' is not listed in the manifest files.")
        
        if not isinstance(hash_value, str):
            raise ValueError(f"Hash value for file '{file}' must be a string.")
        
    return True