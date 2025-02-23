def next_version(version):
    """
    Next version identifier following existing pattern.

    Must deal with both zero-prefixed and non-zero prefixed versions.
    """
    parts = version.split('.')
    for i in reversed(range(len(parts))):
        if parts[i].isdigit():
            parts[i] = str(int(parts[i]) + 1)
            return '.'.join(parts[:i + 1]) + '.' + '.'.join(parts[i + 1:])
    return '1.0'  # Default case if version is empty or invalid