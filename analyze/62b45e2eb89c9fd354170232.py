def next_version(version):
    """
    Prossimo identificatore di versione seguendo il modello esistente.

    Deve gestire sia versioni con prefisso zero che versioni senza prefisso zero.
    """
    # Split the version into parts
    parts = version.split('.')
    
    # Increment the last part
    last_part = int(parts[-1]) + 1
    
    # Handle leading zeros if any
    if parts[-1].startswith('0'):
        # Preserve the leading zeros
        last_part_str = f"{last_part:0{len(parts[-1])}d}"
    else:
        last_part_str = str(last_part)
    
    # Update the last part
    parts[-1] = last_part_str
    
    # Join the parts back together
    return '.'.join(parts)