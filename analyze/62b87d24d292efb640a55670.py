def get_versions():
    """
    获取版本信息。如果无法获取版本信息，则返回默认值。
    获取版本信息或在无法获取时返回默认值
    """
    try:
        # 假设版本信息存储在某个文件或通过某个API获取
        # 这里只是一个示例，实际实现可能需要读取文件或调用API
        version = "1.0.0"  # 假设这是获取到的版本信息
        return version
    except Exception as e:
        # 如果无法获取版本信息，返回默认值
        return "0.0.0"