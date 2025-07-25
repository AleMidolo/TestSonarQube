def next_version(version):
    """
    根据现有模式生成下一个版本标识符

    遵循现有格式的下一个版本标识符
    必须能够处理以零开头和非零开头的两种情况。
    """
    parts = version.split('.')
    for i in reversed(range(len(parts))):
        if parts[i].isdigit():
            parts[i] = str(int(parts[i]) + 1)
            return '.'.join(parts[:i + 1]) + '.' + '.'.join(parts[i + 1:])
    return '1.0'  # Default case if version is empty or invalid