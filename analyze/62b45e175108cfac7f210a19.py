def validate_fixity(self, fixity, manifest_files):
    """
    Convalida l'attributo fixty block nell'inventario.
    
    Controlla la struttura del blocco di fissità e assicurati che siano referenziati solo i file elencati nel manifesto.
    """
    if not isinstance(fixity, dict):
        raise ValueError("Fixity block must be a dictionary")
        
    # Check that all required fields are present
    required_fields = ['messageDigestAlgorithm', 'files']
    for field in required_fields:
        if field not in fixity:
            raise ValueError(f"Missing required field '{field}' in fixity block")
            
    # Validate message digest algorithm
    if not isinstance(fixity['messageDigestAlgorithm'], str):
        raise ValueError("messageDigestAlgorithm must be a string")
        
    # Validate files block
    files = fixity.get('files', {})
    if not isinstance(files, dict):
        raise ValueError("files block must be a dictionary")
        
    # Check that all files referenced exist in manifest
    for filename in files:
        if filename not in manifest_files:
            raise ValueError(f"File '{filename}' in fixity block not found in manifest")
            
        # Validate checksum value
        checksum = files[filename]
        if not isinstance(checksum, str):
            raise ValueError(f"Checksum for file '{filename}' must be a string")
            
    return True