def validate_fixity(self, fixity, manifest_files):
    """
    Convalida l'attributo fixty block nell'inventario.

    Controlla la struttura del blocco di fissità e assicurati che siano referenziati solo i file elencati nel manifesto.
    """
    if not isinstance(fixity, dict):
        raise ValueError("Il blocco di fissità deve essere un dizionario.")
    
    for file_name, checksums in fixity.items():
        if file_name not in manifest_files:
            raise ValueError(f"Il file '{file_name}' non è presente nel manifesto.")
        
        if not isinstance(checksums, dict):
            raise ValueError(f"I checksum per il file '{file_name}' devono essere un dizionario.")
        
        for algorithm, checksum in checksums.items():
            if not isinstance(algorithm, str) or not isinstance(checksum, str):
                raise ValueError(f"L'algoritmo e il checksum per il file '{file_name}' devono essere stringhe.")
    
    return True