def get_versions():
    """
    获取版本信息。如果无法获取版本信息，则返回默认值。
    获取版本信息或在无法获取时返回默认值
    """
    try:
        # 假设版本信息存储在某个文件或通过某个API获取
        # 这里我们模拟一个获取版本信息的操作
        version = "1.0.0"  # 假设这是获取到的版本信息
        return version
    except Exception as e:
        # 如果获取版本信息失败，返回默认值
        default_version = "0.0.0"
        return default_version