def next_version(version):
    """
    Next version identifier following existing pattern.

    Must deal with both zero-prefixed and non-zero prefixed versions.
    """
    # Split the version into parts
    parts = version.split('.')
    
    # Increment the last part
    last_part = int(parts[-1]) + 1
    parts[-1] = str(last_part)
    
    # Handle zero-prefixed versions
    if parts[-1].startswith('0') and len(parts[-1]) > 1:
        parts[-1] = parts[-1].lstrip('0')
        if not parts[-1]:
            parts[-1] = '0'
    
    # Reconstruct the version string
    return '.'.join(parts)