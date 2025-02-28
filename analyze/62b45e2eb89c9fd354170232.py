def next_version(version):
    """
    根据现有模式生成下一个版本标识符

    遵循现有格式的下一个版本标识符
    必须能够处理以零开头和非零开头的两种情况。
    """
    # 将版本字符串转换为整数
    version_num = int(version)
    
    # 增加版本号
    next_version_num = version_num + 1
    
    # 将整数转换回字符串，并保持原有长度
    next_version_str = str(next_version_num).zfill(len(version))
    
    return next_version_str