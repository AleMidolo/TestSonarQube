def validate_fixity(self, fixity, manifest_files):
    """
    Convalida l'attributo fixty block nell'inventario.
    
    Controlla la struttura del blocco di fissità e assicurati che siano referenziati solo i file elencati nel manifesto.
    """
    if not isinstance(fixity, dict):
        raise ValueError("Fixity block must be a dictionary")
        
    # Check that all required fields are present
    required_fields = ['message_digest_algorithm', 'message_digest']
    for field in required_fields:
        if field not in fixity:
            raise ValueError(f"Missing required field '{field}' in fixity block")
            
    # Validate message digest algorithm
    valid_algorithms = ['md5', 'sha1', 'sha256', 'sha512']
    if fixity['message_digest_algorithm'].lower() not in valid_algorithms:
        raise ValueError(f"Invalid message digest algorithm. Must be one of: {valid_algorithms}")
        
    # Validate message digests
    digests = fixity['message_digest']
    if not isinstance(digests, dict):
        raise ValueError("Message digests must be a dictionary")
        
    # Check that all referenced files exist in manifest
    for filename in digests:
        if filename not in manifest_files:
            raise ValueError(f"File '{filename}' referenced in fixity but not found in manifest")
            
    # Validate digest format based on algorithm
    for filename, digest in digests.items():
        if not isinstance(digest, str):
            raise ValueError(f"Digest for file '{filename}' must be a string")
            
        # Check digest length matches algorithm
        expected_length = {
            'md5': 32,
            'sha1': 40, 
            'sha256': 64,
            'sha512': 128
        }[fixity['message_digest_algorithm'].lower()]
        
        if len(digest) != expected_length:
            raise ValueError(f"Invalid digest length for {filename}. Expected {expected_length} characters for {fixity['message_digest_algorithm']}")
            
    return True