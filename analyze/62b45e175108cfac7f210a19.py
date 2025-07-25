def validate_fixity(self, fixity, manifest_files):
    """
    Convalida l'attributo fixty block nell'inventario.

    Controlla la struttura del blocco di fissità e assicurati che siano referenziati solo i file elencati nel manifesto.
    """
    if not isinstance(fixity, dict):
        raise ValueError("Il blocco di fissità deve essere un dizionario.")
    
    for file_name, checksum in fixity.items():
        if file_name not in manifest_files:
            raise ValueError(f"Il file {file_name} non è presente nel manifesto.")
        
        if not isinstance(checksum, str):
            raise ValueError(f"Il checksum per il file {file_name} deve essere una stringa.")
        
        # Puoi aggiungere ulteriori controlli sul formato del checksum se necessario
        # Ad esempio, controllare che sia un hash valido (es. MD5, SHA256, ecc.)
    
    return True