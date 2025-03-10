def next_version(version):
    """
    Next version identifier following existing pattern.

    Must deal with both zero-prefixed and non-zero prefixed versions.
    """
    # Split the version into parts
    parts = version.split('.')
    
    # Increment the last part
    last_part = parts[-1]
    if last_part.isdigit():
        parts[-1] = str(int(last_part) + 1)
    else:
        # Handle non-numeric parts (e.g., 'a', 'b', etc.)
        # Increment the last character
        last_char = last_part[-1]
        if last_char.isalpha():
            if last_char == 'z':
                parts[-1] = last_part[:-1] + 'a'
            else:
                parts[-1] = last_part[:-1] + chr(ord(last_char) + 1)
        else:
            # If the last character is not a letter, append 'a'
            parts[-1] = last_part + 'a'
    
    # Reconstruct the version string
    return '.'.join(parts)