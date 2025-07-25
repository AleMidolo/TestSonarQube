def next_version(version):
    """
    Prossimo identificatore di versione seguendo il modello esistente.

    Deve gestire sia versioni con prefisso zero che versioni senza prefisso zero.
    """
    # Split the version into parts
    parts = version.split('.')
    
    # Convert parts to integers
    parts = [int(part) for part in parts]
    
    # Increment the last part
    parts[-1] += 1
    
    # Handle carry-over for parts with leading zeros
    for i in range(len(parts) - 1, 0, -1):
        if parts[i] > 9:
            parts[i] = 0
            parts[i - 1] += 1
    
    # Convert parts back to strings
    parts = [str(part) for part in parts]
    
    # Join the parts with '.' to form the new version
    new_version = '.'.join(parts)
    
    return new_version