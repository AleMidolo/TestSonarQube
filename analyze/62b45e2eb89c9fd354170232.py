def next_version(version):
    parts = version.split('.')
    for i in reversed(range(len(parts))):
        if parts[i].lstrip('0') == '':
            parts[i] = '1'
            return '.'.join(parts)
        elif int(parts[i]) < 9:
            parts[i] = str(int(parts[i]) + 1)
            return '.'.join(parts[:i + 1]) + '.' + '.'.join(parts[i + 1:])
        else:
            parts[i] = '0'
    return '1.' + '.'.join(parts)