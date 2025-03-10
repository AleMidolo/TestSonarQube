def get_versions():
    """
    获取版本信息。如果无法获取版本信息，则返回默认值。
    获取版本信息或在无法获取时返回默认值
    """
    try:
        # 假设版本信息是从某个地方获取的，这里用模拟数据代替
        version_info = {
            "version": "1.0.0",
            "build_date": "2023-10-01",
            "commit_hash": "abc123"
        }
        return version_info
    except Exception as e:
        # 如果获取版本信息失败，返回默认值
        return {
            "version": "unknown",
            "build_date": "unknown",
            "commit_hash": "unknown"
        }