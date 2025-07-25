def next_version(version):
    """
    Prossimo identificatore di versione seguendo il modello esistente.

    Deve gestire sia versioni con prefisso zero che versioni senza prefisso zero.
    """
    # Split the version into parts
    parts = version.split('.')
    
    # Increment the last part
    last_part = int(parts[-1]) + 1
    parts[-1] = str(last_part)
    
    # Handle the case where the last part overflows (e.g., 9 -> 10)
    for i in range(len(parts) - 1, 0, -1):
        if int(parts[i]) > 9:
            parts[i] = '0'
            parts[i - 1] = str(int(parts[i - 1]) + 1
    
    # Handle the case where the first part overflows (e.g., 9 -> 10)
    if int(parts[0]) > 9:
        parts[0] = '10'
    
    # Reconstruct the version string
    return '.'.join(parts)