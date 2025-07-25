def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifique que todos los resúmenes necesarios en el manifiesto estén presentes y se utilicen.
    """
    required_digests = set()
    
    # Recolectar todos los resúmenes necesarios de los archivos de manifiesto
    for manifest in manifest_files:
        with open(manifest, 'r') as file:
            for line in file:
                digest = line.strip()
                if digest:
                    required_digests.add(digest)
    
    # Verificar que todos los resúmenes necesarios se utilicen
    missing_digests = required_digests - set(digests_used)
    
    if missing_digests:
        raise ValueError(f"Faltan los siguientes resúmenes: {missing_digests}")
    
    return True