def get_versions():
    """
    获取版本信息。如果无法获取版本信息，则返回默认值。
    获取版本信息或在无法获取时返回默认值
    """
    try:
        # 尝试获取版本信息
        import pkg_resources
        versions = {}
        
        # 获取已安装包的版本信息
        installed_packages = pkg_resources.working_set
        for package in installed_packages:
            versions[package.key] = package.version
            
        return versions
        
    except Exception:
        # 如果获取失败,返回默认值
        return {
            'python': '3.x',
            'pip': 'unknown',
            'setuptools': 'unknown'
        }