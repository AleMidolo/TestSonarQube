def next_version(version):
    """
    根据现有模式生成下一个版本标识符

    遵循现有格式的下一个版本标识符
    必须能够处理以零开头和非零开头的两种情况。
    """
    parts = list(map(int, version.split('.')))
    parts[-1] += 1  # Increment the last part
    for i in reversed(range(len(parts))):
        if parts[i] >= 10:  # Assuming version parts are single digits
            parts[i] = 0
            if i > 0:
                parts[i - 1] += 1
    return '.'.join(map(str, parts))