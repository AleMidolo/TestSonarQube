def get_versions():
    """
    获取版本信息。如果无法获取版本信息，则返回默认值。
    获取版本信息或在无法获取时返回默认值
    """
    import sys
    try:
        # 尝试获取 Python 版本信息
        version_info = sys.version_info
        return f"Python {version_info.major}.{version_info.minor}.{version_info.micro}"
    except Exception as e:
        # 如果无法获取版本信息，返回默认值
        return "Unknown version"