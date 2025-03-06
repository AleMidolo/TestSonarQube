def next_version(version):
    """
    Prossimo identificatore di versione seguendo il modello esistente.

    Deve gestire sia versioni con prefisso zero che versioni senza prefisso zero.
    """
    # Split the version into parts
    parts = version.split('.')
    
    # Increment the last part
    last_part = int(parts[-1]) + 1
    
    # Handle the case where the last part was a zero-prefixed number
    if parts[-1].startswith('0'):
        # Preserve the zero prefix by formatting the incremented number with the same length
        parts[-1] = f"{last_part:0{len(parts[-1])}d}"
    else:
        parts[-1] = str(last_part)
    
    # Join the parts back together
    return '.'.join(parts)