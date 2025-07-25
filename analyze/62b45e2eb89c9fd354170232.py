def next_version(version):
    """
    Next version identifier following existing pattern.

    Must deal with both zero-prefixed and non-zero prefixed versions.
    """
    # Split the version into parts
    parts = version.split('.')
    
    # Increment the last part
    last_part = int(parts[-1]) + 1
    
    # Handle zero-prefixed versions
    if parts[-1].startswith('0'):
        # Preserve the zero-prefix length
        zero_prefix_length = len(parts[-1]) - len(str(int(parts[-1])))
        parts[-1] = '0' * zero_prefix_length + str(last_part)
    else:
        parts[-1] = str(last_part)
    
    # Join the parts back together
    return '.'.join(parts)