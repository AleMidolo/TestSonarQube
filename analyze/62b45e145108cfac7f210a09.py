def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifique que todos los resúmenes necesarios en el manifiesto estén presentes y se utilicen.
    
    Args:
        manifest_files (list): Lista de archivos de manifiesto.
        digests_used (set): Conjunto de resúmenes utilizados.
    
    Returns:
        bool: True si todos los resúmenes necesarios están presentes y se utilizan, False en caso contrario.
    """
    # Obtener todos los resúmenes necesarios del manifiesto
    required_digests = set()
    for manifest_file in manifest_files:
        with open(manifest_file, 'r') as file:
            for line in file:
                if line.strip():
                    required_digests.add(line.strip())
    
    # Verificar que todos los resúmenes necesarios estén presentes
    if not required_digests.issubset(digests_used):
        return False
    
    # Verificar que todos los resúmenes utilizados estén en los necesarios
    if not digests_used.issubset(required_digests):
        return False
    
    return True