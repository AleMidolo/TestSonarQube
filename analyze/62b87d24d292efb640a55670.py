def get_versions():
    """
    获取版本信息。如果无法获取版本信息，则返回默认值。
    获取版本信息或在无法获取时返回默认值
    """
    try:
        import pkg_resources
        versions = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
        return versions
    except Exception:
        return {"default": "1.0.0"}