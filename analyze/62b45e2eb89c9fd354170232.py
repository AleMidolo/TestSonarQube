def next_version(version):
    """
    Prossimo identificatore di versione seguendo il modello esistente.

    Deve gestire sia versioni con prefisso zero che versioni senza prefisso zero.
    """
    # Split the version into parts
    parts = version.split('.')
    
    # Increment the last part
    last_part = int(parts[-1]) + 1
    
    # Handle the case where the last part overflows (e.g., 9 -> 10)
    if last_part > 9:
        parts[-1] = '0'
        if len(parts) > 1:
            # Increment the next higher part
            for i in range(len(parts) - 2, -1, -1):
                parts[i] = str(int(parts[i]) + 1)
                if int(parts[i]) <= 9:
                    break
                else:
                    parts[i] = '0'
                    if i == 0:
                        # If the first part overflows, prepend a '1'
                        parts.insert(0, '1')
    else:
        parts[-1] = str(last_part)
    
    # Reconstruct the version string
    return '.'.join(parts)