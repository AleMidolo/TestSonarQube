def next_version(version):
    """
    Prossimo identificatore di versione seguendo il modello esistente.

    Deve gestire sia versioni con prefisso zero che versioni senza prefisso zero.
    """
    parts = version.split('.')
    for i in reversed(range(len(parts))):
        if parts[i] != '9':
            parts[i] = str(int(parts[i]) + 1)
            return '.'.join(parts[:i + 1]) + '.' + '.'.join(parts[i + 1:])
        parts[i] = '0'
    return '1.' + '.'.join(parts)