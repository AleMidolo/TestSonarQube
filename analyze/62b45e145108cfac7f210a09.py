def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifique que todos los resúmenes necesarios en el manifiesto estén presentes y se utilicen.
    
    Args:
        manifest_files (list): Lista de archivos de manifiesto que contienen los resúmenes.
        digests_used (set): Conjunto de resúmenes que se han utilizado.
    
    Returns:
        bool: True si todos los resúmenes necesarios están presentes y se utilizan, False en caso contrario.
    """
    # Extraer todos los resúmenes presentes en los archivos de manifiesto
    digests_present = set()
    for manifest_file in manifest_files:
        with open(manifest_file, 'r') as file:
            for line in file:
                if line.strip():  # Ignorar líneas vacías
                    digests_present.add(line.strip())
    
    # Verificar que todos los resúmenes necesarios estén presentes
    if not digests_used.issubset(digests_present):
        return False
    
    # Verificar que todos los resúmenes presentes se utilicen
    if not digests_present.issubset(digests_used):
        return False
    
    return True